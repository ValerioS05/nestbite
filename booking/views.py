from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.dateparse import parse_date
from datetime import datetime, timedelta
from decimal import Decimal
from .forms import BookingForm, ReviewForm
from .models import Booking, Review
from restaurants.models import Restaurant, Table


def check_timings(booking, restaurant, form):
    """
    Checks that the booking timings are within the restaurant's operating hours
    and also checks the minimum and maximum stay duration.

    Args:
        booking (Booking): The booking instance being validated.
        restaurant (Restaurant): The restaurant instance for checking working hours.
        form (BookingForm): The form containing the booking details.

    Return:
        bool: True if the checks are valid, False otherwise.
    """
    start_time = booking.start_time
    end_time = booking.end_time
    opening_time = restaurant.opening_time
    closing_time = restaurant.closing_time

    if start_time < opening_time or end_time > closing_time:
        form.add_error(
            None,
            "Your booking must be within the restaurant's working hours."
        )
        return False

    one_hour_before_closing = (
        datetime.combine(booking.booking_date, closing_time)
        - timedelta(hours=1)
    ).time()

    if start_time > one_hour_before_closing:
        form.add_error(
            None,
            f"Bookings must start at least one hour before closing time "
            f"({one_hour_before_closing})."
        )
        return False

    duration = (
        datetime.combine(booking.booking_date, end_time)
        - datetime.combine(booking.booking_date, start_time)
    ).total_seconds() / 3600

    if duration < 1:
        form.add_error(None, "The minimum stay for a booking is 1 hour.")
        return False

    if duration > 3:
        form.add_error(None, "The maximum stay for a booking is 3 hours.")
        return False

    return True


def overlapping_bookings(booking, form, current_booking=None):
    """
    Check for overlapping bookings for the selected tables during the specified
    time window (start_time to end_time).
    Considering the possibility that the 
    current booking is an update to an existing booking (in this
    case, it excludes that booking from the overlap check).

    Args:
        booking (Booking): The booking instance being checked.
        form (BookingForm): The form containing the booking details.
        current_booking (Booking, optional): The current booking instance being
        updated. Defaults to None.

    Returns:
        bool: True if there are overlapping bookings for the selected tables 
        during the specified time, False otherwise. If an overlap is 
        found, the function suggests alternative available tables 
        within a similar price range and capacity.
    """
    if not booking.id:
        selected_tables = form.cleaned_data['tables']
    else:
        selected_tables = booking.tables.all()

    overlapping_bookings = Booking.objects.filter(
        tables__in=selected_tables,
        canceled=False,
        booking_date=booking.booking_date,
        start_time__lt=booking.end_time,
        end_time__gt=booking.start_time
    )

    if current_booking:
        overlapping_bookings = overlapping_bookings.exclude(
            id=current_booking.id)

    if overlapping_bookings.exists():
        form.add_error(
            None,
            "The selected tables are already booked during the specified time."
        )
        unavailable_tables = overlapping_bookings.values_list(
            'tables', flat=True)
        selected_table_prices = selected_tables.values_list(
            'price', flat=True)
        selected_table_prices = [
            Decimal(price) for price in selected_table_prices
        ]
        price_min = min(selected_table_prices) * Decimal('0.9')
        price_max = max(selected_table_prices) * Decimal('1.1')

        suggested_tables = Table.objects.exclude(
            id__in=unavailable_tables).filter(
            price__gte=price_min, price__lte=price_max
        )[:4]

        if suggested_tables.exists():
            suggestion_list = ', '.join(
                f"{table} (Max: {table.capacity})"
                for table in suggested_tables
            )
            form.add_error(
                None,
                f"Consider one of these available tables: {suggestion_list}."
            )
        return True
    return False


def handle_booking_form(request, form, restaurant, booking=None):
    """
    Handle form submission/validation for creating/updating a booking.
    The function checks the validity of the form data, ensures that the booking
    is within restaurant hours and that there are no overlapping bookings
    for the selected table(s). If the booking is valid, it saves the data to the
    database.

    Args:
        request (HttpRequest): The current HTTP request.
        form (BookingForm): The form containing the booking details.
        restaurant (Restaurant): The restaurant connected to the booking.
        booking (Booking, optional): The existing booking being updated.
        Defaults to None.

    Returns:
        tuple: A tuple containing a boolean indicating success, and either the
        booking instance or the form with errors. This depends on the result 
        of the form submission, if the form is valid the function redirect
        to the right view. If unsuccesfull renders the form with errors.
    """
    if form.is_valid():
        booking_instance = form.save(commit=False)

        if booking:
            booking_instance.id = booking.id
            booking_instance.customer_email = booking.customer_email
            booking_instance.user = booking.user
        else:

            booking_instance.customer_email = request.user.email
            booking_instance.user = request.user

        booking_instance.customer_name = form.cleaned_data['customer_name']
        booking_instance.booking_date = form.cleaned_data['booking_date']

        if not check_timings(booking_instance, restaurant, form):
            return False, form

        if overlapping_bookings(
                booking_instance, form, current_booking=booking):
            return False, form

        if booking:
            booking.start_time = booking_instance.start_time
            booking.end_time = booking_instance.end_time
            booking.tables.set(form.cleaned_data['tables'])
            booking.message = booking_instance.message
            booking.customer_name = booking_instance.customer_name
            booking.booking_date = booking_instance.booking_date
            booking.save()
        else:
            booking_instance.save()
            form.save_m2m()

        return True, booking_instance
    return False, form


@login_required
def create_booking(request, restaurant_id):
    """
    Create a new booking for a specific restaurant
    by processing the form.

    Args:
        request (HttpRequest): The current HTTP request.
        restaurant_id (int): The ID of the restaurant.

    Returns:
        HttpResponse: The rendered booking form or a redirect on success.
    """
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, restaurant_id=restaurant_id)
        success, booking = handle_booking_form(request, form, restaurant)

        if success:
            table_names = ', '.join(str(table)
                                    for table in booking.tables.all())
            messages.success(
                request,
                f'Your booking is confirmed! See you soon.'

            )
            return redirect('booking_list')
    else:
        form = BookingForm(restaurant_id=restaurant.id)

    return render(
        request, 'booking/booking_form.html',
        {'form': form, 'restaurant': restaurant}
    )


@login_required
def update_booking(request, booking_id):
    """
    Update an existing booking.

    Args:
        request (HttpRequest): The current HTTP request.
        booking_id (int): The ID of the booking to be updated.

    Returns:
        HttpResponse: The rendered update form or a redirect on success.
    """
    booking = get_object_or_404(Booking, id=booking_id)

    if not (
            request.user.is_staff or
            booking.customer_email == request.user.email):
        messages.error(request, "You are not allowed to modify this booking.")
        return redirect('booking_list')

    restaurant = booking.tables.first().restaurant

    if request.method == 'POST':
        form = BookingForm(request.POST, restaurant_id=restaurant.id)
        success, booking_instance = handle_booking_form(
            request, form, restaurant, booking
        )

        if success:
            table_names = ', '.join(str(table)
                                    for table in booking_instance.tables.all())
            messages.success(
                request,
                f'Your booking has been updated successfully!.'
            )
            return redirect('booking_list')
    else:
        form = BookingForm(
            initial={
                'tables': booking.tables.all(),
                'customer_name': booking.customer_name,
                'booking_date': booking.booking_date,
                'start_time': booking.start_time,
                'end_time': booking.end_time,
                'message': booking.message,
            },
            restaurant_id=restaurant.id
        )

    return render(
        request, 'booking/update_booking_form.html',
        {'form': form, 'restaurant': restaurant}
    )


@login_required
def booking_list(request):
    """
    Display the list of bookings for the current user.
    Admin can see all bookings.

    Args:
        request (HttpRequest): The current HTTP request.

    Returns:
        HttpResponse: The rendered booking list.
    """
    user = request.user
    filter_date_str = request.GET.get('filter_date', None)
    filter_date = None

    if user.is_staff:
        bookings = Booking.objects.filter(canceled=False)
    else:
        bookings = Booking.objects.filter(customer_email=user.email, canceled=False)

    if filter_date_str:
        filter_date = parse_date(filter_date_str)
        if filter_date:
            bookings = bookings.filter(booking_date=filter_date)

    return render(
        request, 'booking/booking_list.html',
        {'bookings': bookings, 'filter_date': filter_date_str}
    )


@login_required
def booking_detail(request, booking_id):
    """
    Display the details of a specific booking and handle review.

    Args:
        request (HttpRequest): The current HTTP request.
        booking_id (int): The ID of the booking.

    Returns:
        HttpResponse: The rendered booking details and review form.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    is_owner = booking.customer_email == request.user.email

    if not (request.user.is_staff or is_owner):
        return redirect('booking_list')

    existing_review = booking.reviews.filter(user=request.user).first()

    if request.method == 'POST':
        if existing_review:
            return redirect('booking_detail', booking_id=booking.id)

        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.booking = booking
            review.restaurant = booking.tables.first().restaurant
            review.user = request.user
            review.save()

            booking_reference = booking.booking_reference
            send_mail(
                subject=f'New review for Booking: {booking_reference}',
                message=(
                    f'Restaurant: {review.restaurant.name}\n'
                    f'User: {review.user.username}\n'
                    f'Rating: {review.rating}\n'
                    f'Message: {review.message}'
                ),
                from_email='nestbite@gmail.com',
                recipient_list=['nestbite@gmail.com'],
                fail_silently=False,
            )

            feedback_message = (
                "Thanks for your feedback! It's great to make you happy!"
                if review.rating >= 4
                else "We appreciate your feedback and will work to improve!"
            )

            messages.success(request, feedback_message)
            return redirect('booking_list')
    else:
        review_form = ReviewForm() if is_owner and not existing_review else None

    return render(
        request, 'booking/booking_detail.html',
        {
            'booking': booking,
            'review_form': review_form,
            'existing_review': existing_review,
            'feedback_message': None,
        }
    )


@login_required
def cancel_booking(request, booking_id):
    """
    Cancel an existing booking.

    Args:
        request (HttpRequest): The current HTTP request.
        booking_id (int): The ID of the booking to be canceled.

    Returns:
        HttpResponse: Redirects to the booking list on success.
    """
    booking = get_object_or_404(Booking, id=booking_id)

    if not (request.user.is_staff or booking.customer_email == request.user.email):
        messages.error(request, "You are not allowed to cancel this booking.")
        return redirect('booking_list')
    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Your booking has been successfully canceled.")
        return redirect('booking_list')

    return render(request, 'booking/cancel_booking.html', {'booking': booking})

def delete_finished_booking(booking_id):
    """
    Delete a booking if it's finished and two hours passed since
    the booking end time.

    Args:
        booking_id (int): The ID of the booking to be checked and possibly deleted.

    Returns:
        bool: True if the booking was deleted, False otherwise.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking_datetime = timezone.make_aware(
        datetime.combine(booking.booking_date, booking.end_time)
    )
    delete_time = booking_datetime + timedelta(hours=2)
    now = timezone.now()
    if now >= delete_time:
        booking.delete()
        return True
    return False
