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
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, restaurant_id=restaurant.id)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer_email = request.user.email  # Set customer email
            booking.user = request.user  # Assign the logged-in user
            booking.save()

            # Save the many-to-many relationship for tables
            form.save_m2m()

            messages.success(request, 'Your booking has been created successfully!')
            return redirect('booking_list')
    else:
        form = BookingForm(restaurant_id=restaurant.id)

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