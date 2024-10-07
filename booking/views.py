from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta
from .forms import BookingForm
from .models import Booking

@login_required
def booking_list(request):
    if request.user.is_staff:
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(customer_email=request.user.email)  # Use customer_email to match with user
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

@login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if not (request.user.is_staff or booking.customer_email == request.user.email):
        return redirect('booking_list')
    return render(request, 'booking/booking_detail.html', {'booking': booking})

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer_email = request.user.email  # Use customer_email to store the user email

            
            booking.save()

           
            overlapping_bookings = Booking.objects.filter(
                tables__in=booking.tables.all(),
                booking_date=booking.booking_date,
                start_time__lt=booking.end_time,
                end_time__gt=booking.start_time
            ).exclude(pk=booking.pk)

            if overlapping_bookings.exists():
                booking.delete()  
                form.add_error(None, "One or more tables are already booked during this time slot.")
                return render(request, 'booking/booking_form.html', {'form': form})

            
            form.save_m2m()

            messages.success(request, 'Your booking has been created successfully!')
            return redirect('booking_list')
    else:
        form = BookingForm()
    
    return render(request, 'booking/booking_form.html', {'form': form})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Check right to cancel
    if not (request.user.is_staff or booking.customer_email == request.user.email):
        messages.error(request, "You are not allowed to cancel this booking.")
        return redirect('booking_list')

    
    if request.method == 'POST':
        # Create a timezone-aware datetime for the booking
        booking_datetime = timezone.make_aware(datetime.combine(booking.booking_date, booking.start_time))

        # Get the current time
        now = timezone.now()

        # Compare the times
        if booking_datetime < now + timedelta(hours=2):
            messages.error(request, "You can only cancel bookings at least 2 hours in advance.")
            return redirect('booking_detail', booking_id=booking.id)

        # Cancel the booking
        booking.delete()
        messages.success(request, "Your booking has been canceled successfully.")
        return redirect('booking_list')

    return render(request, 'booking/cancel_booking.html', {'booking': booking})