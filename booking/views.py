from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta
from .forms import BookingForm
from .models import Booking
from restaurants.models import Restaurant


@login_required
def booking_list(request):
    if request.user.is_staff:
        bookings = Booking.objects.all()  # Retrieve all bookings for staff
    else:
        bookings = Booking.objects.filter(customer_email=request.user.email)  # Filter by the user's email

    return render(request, 'booking/booking_list.html', {'bookings': bookings})

@login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if not (request.user.is_staff or booking.customer_email == request.user.email):
        return redirect('booking_list')
    return render(request, 'booking/booking_detail.html', {'booking': booking})

@login_required
def create_booking(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)  # Get the restaurant instance

    if request.method == 'POST':
        form = BookingForm(request.POST, restaurant_id=restaurant_id)  # Pass restaurant_id to the form
        if form.is_valid():
            # Create a Booking instance but do not save it to the database yet
            booking = form.save(commit=False)

            booking.customer_email = request.user.email
            booking.user = request.user  # Assign the logged-in user

            # Extract the start and end times for overlap checking
            start_time = booking.start_time
            end_time = booking.end_time

            # Check restaurant's opening hours
            opening_time = restaurant.opening_time
            closing_time = restaurant.closing_time

            # Ensure booking is within the restaurant's hours
            if start_time < opening_time or end_time > closing_time:
                form.add_error(None, "Your booking must be within the restaurant's working hours.")
                return render(request, 'booking/booking_form.html', {'form': form, 'restaurant': restaurant})

            # Ensure the booking starts at least 1 hour before closing time
            one_hour_before_closing = (datetime.combine(booking.booking_date, closing_time) - timedelta(hours=1)).time()
            if start_time > one_hour_before_closing:
                form.add_error(None, f"Bookings must start at least one hour before closing time ({one_hour_before_closing}).")
                return render(request, 'booking/booking_form.html', {'form': form, 'restaurant': restaurant})

            # Calculate the duration of the booking
            duration = (datetime.combine(booking.booking_date, end_time) - 
                        datetime.combine(booking.booking_date, start_time)).total_seconds() / 3600  # Convert to hours

            # Check for minimum and maximum stay duration
            if duration < 1:  # Minimum stay of 1 hour
                form.add_error(None, "The minimum stay for a booking is 1 hour.")
                return render(request, 'booking/booking_form.html', {'form': form, 'restaurant': restaurant})

            if duration > 3:  # Maximum stay of 3 hours
                form.add_error(None, "The maximum stay for a booking is 3 hours.")
                return render(request, 'booking/booking_form.html', {'form': form, 'restaurant': restaurant})

            # Check for overlapping bookings for the selected tables
            overlapping_bookings = Booking.objects.filter(
                tables__in=form.cleaned_data['tables'],  # Get tables from cleaned data
                canceled=False,  # Only consider active bookings
                booking_date=booking.booking_date,
                start_time__lt=end_time,  # New booking starts before existing booking ends
                end_time__gt=start_time     # New booking ends after existing booking starts
            )

            if overlapping_bookings.exists():
                # If there are overlapping bookings, show an error and re-render the form
                form.add_error(None, "The selected tables are already booked during the specified time.")
                # Render the form again with the error message
                return render(request, 'booking/booking_form.html', {'form': form, 'restaurant': restaurant})

            # Save the booking now that we know there are no overlaps
            booking.save()  # Now save the booking to the database
            
            # Save the many-to-many relationship for tables
            form.save_m2m()

            # Prepare the table names for the success message
            table_names = ', '.join(str(table) for table in booking.tables.all())
            messages.success(request, f'Your booking for the following table(s) has been created successfully: {table_names}.')
            
            return redirect('booking_list')  # Redirect to the booking list after successful booking

    else:
        form = BookingForm(restaurant_id=restaurant.id)  # Create form instance for GET request

    return render(request, 'booking/booking_form.html', {'form': form, 'restaurant': restaurant})





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

    return render(request, 'booking/cancel_booking.html', {'booking': booking})