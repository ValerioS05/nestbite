from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from restaurants.models import Table
import random
import string

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')  # Connect Booking to User
    tables = models.ManyToManyField(Table, related_name='bookings')
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    message = models.TextField(blank=True, null=True)
    booking_reference = models.CharField(max_length=10, unique=True, blank=True, null=True)
    canceled = models.BooleanField(default=False)

    def clean(self):
        if self.start_time is None:
            raise ValidationError("Start time cannot be None.")
        if self.end_time is None:
            raise ValidationError("End time cannot be None.")
        booking_datetime_start = timezone.make_aware(datetime.combine(self.booking_date, self.start_time))
        now = timezone.now()
        # Calculate twelve months from now
        twelve_months_later = now + timedelta(days=365)
        
        # Check if the booking is in the past
        if booking_datetime_start < now:
            raise ValidationError("Cannot book in the past.")
        # Check if the booking is at least 2 hours in advance
        if booking_datetime_start < now + timedelta(hours=2):
            raise ValidationError("Bookings must be made at least 2 hours in advance.")
        # Check if the booking date is within the next 12 months
        if booking_datetime_start > twelve_months_later:
            raise ValidationError("Bookings can only be made for up to 12 months in advance.")

    @staticmethod
    def generate_booking_reference():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def save(self, *args, **kwargs):
        if not self.booking_reference:
            self.booking_reference = Booking.generate_booking_reference()
        super().save(*args, **kwargs)


    # Calculate the total price of the booking based on the tables booked
    @property
    def total_price(self):
        return sum(table.price for table in self.tables.all())


    def cancel(self):
        """Cancels the booking if it's at least 2 hours before the booking time."""
        booking_datetime = timezone.make_aware(datetime.combine(self.booking_date, self.start_time))
        now = timezone.now()

        # Check if the booking can be canceled (at least 2 hours before)
        if booking_datetime < now + timedelta(hours=2):
            raise ValidationError("You can only cancel your booking 2 hours in advance.")

        self.canceled = True
        self.save()

    def __str__(self):
        return f"Booking {self.booking_reference} for {self.customer_name} on {self.booking_date}"