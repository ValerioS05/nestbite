from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from django.contrib import messages


# Create your views here.
@login_required
def booking_list(request):
    if request.user.is_staff:
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

@login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if not (request.user.is_staff or booking.user == request.user):
        return redirect('booking_list')
    return render(request, 'booking/booking_detail.html', {'booking': booking})



@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been created successfully!')
            return redirect('booking_list')
    else:
        form = BookingForm()
    
    return render(request, 'booking/booking_form.html', {'form': form})