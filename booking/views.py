from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.utils.dateparse import parse_date
from datetime import datetime, timedelta
from decimal import Decimal
from .forms import BookingForm
from .forms import ReviewForm
from .models import Booking, Review
from restaurants.models import Restaurant, Table


# Check if the booking is within restaurant hours and constraints
def check_timings(booking, restaurant, form):
    start_time = booking.start_time
    end_time = booking.end_time
    opening_time = restaurant.opening_time
    closing_time = restaurant.closing_time

    # Ensure booking is within the restaurant's hours
    if start_time < opening_time or end_time > closing_time:
        form.add_error(None, "Your booking must be within the restaurant's working hours.")
        return False

    # Ensure the booking starts at least 1 hour before closing time
    one_hour_before_closing = (datetime.combine(booking.booking_date, closing_time) - timedelta(hours=1)).time()
    if start_time > one_hour_before_closing:
        form.add_error(None, f"Bookings must start at least one hour before closing time ({one_hour_before_closing}).")
        return False

    # Calculate duration and check minimum and maximum stay duration
    duration = (datetime.combine(booking.booking_date, end_time) - 
                datetime.combine(booking.booking_date, start_time)).total_seconds() / 3600  # Convert to hours

    if duration < 1:
        form.add_error(None, "The minimum stay for a booking is 1 hour.")
        return False

    if duration > 3:
        form.add_error(None, "The maximum stay for a booking is 3 hours.")
        return False

    return True


# Check for overlapping bookings for the selected tables
def overlapping_bookings(booking, form, current_booking=None):
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

    # If updating, exclude the current booking from the overlap check
    if current_booking:
        overlapping_bookings = overlapping_bookings.exclude(id=current_booking.id)

    if overlapping_bookings.exists():
        form.add_error(None, "The selected tables are already booked during the specified time.")
        unavailable_tables = overlapping_bookings.values_list('tables', flat=True)
        selected_table_prices = selected_tables.values_list('price', flat=True)
        selected_table_prices = [Decimal(price) for price in selected_table_prices]
        price_min = min(selected_table_prices) * Decimal('0.9')
        price_max = max(selected_table_prices) * Decimal('1.1')
        suggested_tables = Table.objects.exclude(id__in=unavailable_tables).filter(
            price__gte=price_min,
            price__lte=price_max
        )[:4]  # Limit to max of 4 suggestions
        if suggested_tables.exists():
            suggestion_list = ', '.join(
                f"{table} (Max: {table.capacity})" for table in suggested_tables
            )
            form.add_error(None, f"Consider booking one of these available tables: {suggestion_list}.")
        return True
    return False


#  Handle booking form
def handle_booking_form(request, form, restaurant, booking=None):
    if form.is_valid():
        # Create or update a Booking instance but do not save it to the database yet
        booking_instance = form.save(commit=False)
        
        # If updating copy over existing values
        if booking:
            booking_instance.id = booking.id
            booking_instance.customer_email = booking.customer_email
            booking_instance.user = booking.user
        else:
            # For new bookings, assign the user
            booking_instance.customer_email = request.user.email
            booking_instance.user = request.user

        # Check time constraints using the existing logic
        if not check_timings(booking_instance, restaurant, form):
            return False, form

        # Pass the current booking to the overlapping check
        if overlapping_bookings(booking_instance, form, current_booking=booking):
            return False, form

        # Save the booking
        if booking:
            booking.start_time = booking_instance.start_time
            booking.end_time = booking_instance.end_time
            booking.tables.set(form.cleaned_data['tables'])  # Update the many-to-many relationship using cleaned data
            booking.message = booking_instance.message  # Update message if any
            booking.save()  # Save the updated booking
        else:
            booking_instance.save()  # Save the new booking
            form.save_m2m()  # Save the many-to-many relationship for tables

        return True, booking_instance
    return False, form



@login_required
def create_booking(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)  # Get the restaurant instance

    if request.method == 'POST':
        form = BookingForm(request.POST, restaurant_id=restaurant_id)  # Pass restaurant_id to the form
        success, booking = handle_booking_form(request, form, restaurant)

        if success:
            # Prepare the table names for the success message
            table_names = ', '.join(str(table) for table in booking.tables.all())
            messages.success(request, f'Your booking for the following table(s) has been created successfully: {table_names}.')
            return redirect('booking_list')  # Redirect to the booking list after successful booking
    else:
        form = BookingForm(restaurant_id=restaurant.id)  # Create form instance for GET request

    return render(request, 'booking/booking_form.html', {'form': form, 'restaurant': restaurant})


@login_required
def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Check right to modify
    if not (request.user.is_staff or booking.customer_email == request.user.email):
        messages.error(request, "You are not allowed to modify this booking.")
        return redirect('booking_list')

    restaurant = booking.tables.first().restaurant

    if request.method == 'POST':
        form = BookingForm(request.POST, restaurant_id=restaurant.id)

        success, booking_instance = handle_booking_form(request, form, restaurant, booking)

        if success:
            # Prepare the table names for the success message
            table_names = ', '.join(str(table) for table in booking_instance.tables.all())
            messages.success(request, f'Your booking has been updated successfully: {table_names}.')
            return redirect('booking_list')  # Redirect to the booking list after successful update
    else:
        form = BookingForm(initial={
            'tables': booking.tables.all(),
            'customer_name': booking.customer_name,
            'booking_date': booking.booking_date,
            'start_time': booking.start_time,
            'end_time': booking.end_time,
            'message': booking.message,
        }, restaurant_id=restaurant.id)

    return render(request, 'booking/update_booking_form.html', {'form': form, 'restaurant': restaurant})


@login_required
def booking_list(request):
    user = request.user
    filter_date_str = request.GET.get('filter_date', None)
    filter_date = None

    if filter_date_str:
        filter_date = parse_date(filter_date_str)

    if user.is_staff:
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(customer_email=user.email)

    if filter_date:
        bookings = bookings.filter(booking_date=filter_date)

    for booking in bookings:
        delete_finished_booking(booking.id)

    return render(request, 'booking/booking_list.html', {'bookings': bookings, 'filter_date': filter_date_str})


@login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if not (request.user.is_staff or booking.customer_email == request.user.email):
        return redirect('booking_list')
    existing_review = booking.reviews.filter(user=request.user).first()
    if request.method == 'POST':
        if existing_review:
            messages.info(request, "You have already submitted feedback for this booking.")
            return redirect('booking_detail', booking_id=booking.id)
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.booking = booking
            review.restaurant = booking.tables.first().restaurant
            review.user = request.user
            review.save()
            if review.rating >= 4:
                feedback_message = "Thanks for your feedback! It's great to make you happy!"
            else:
                feedback_message = "We appreciate your feedback and will work to improve!"

            return redirect('booking_detail', booking_id=booking.id)
    else:
        review_form = ReviewForm() if not existing_review else None

    return render(request, 'booking/booking_detail.html', {
        'booking': booking,
        'review_form': review_form,
        'existing_review': existing_review,
        'feedback_message': None,
    })


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Check right to cancel
    if not (request.user.is_staff or booking.customer_email == request.user.email):
        messages.error(request, "You are not allowed to cancel this booking.")
        return redirect('booking_list')

    if request.method == 'POST':
        booking_datetime = timezone.make_aware(datetime.combine(booking.booking_date, booking.start_time))
        now = timezone.now()

        if booking_datetime < now + timedelta(hours=2):
            messages.error(request, "You can only cancel bookings at least 2 hours in advance.")
            return redirect('booking_detail', booking_id=booking.id)

        booking.delete()
        messages.success(request, "Your booking has been canceled successfully.")
        return redirect('booking_list')

    # Render the cancel confirmation page for GET request
    return render(request, 'booking/cancel_booking.html', {'booking': booking})



def delete_finished_booking(booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking_datetime = timezone.make_aware(datetime.combine(booking.booking_date, booking.end_time))
    delete_time = booking_datetime + timedelta(hours=2)
    now = timezone.now()
    if now >= delete_time:
        booking.delete()
        return True
    return False