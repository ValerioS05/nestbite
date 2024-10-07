from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta
from restaurants.models import Table
import random
import string

class Booking(models.Model):
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
        # Check if booking is not in the past
        booking_datetime = datetime.combine(self.booking_date, self.start_time)
        now = timezone.now()
        if booking_datetime < now:
            raise ValidationError("Cannot book in the past.")

        # Check if booking is at least 2 hours in the future
        if booking_datetime < now + timedelta(hours=2):
            raise ValidationError("Bookings must be made at least 2 hours in advance.")

        # Ensure the booking is within restaurant hours
        for table in self.tables.all():
            if self.start_time < table.restaurant.opening_time or self.end_time > table.restaurant.closing_time:
                raise ValidationError(f"Booking time must be within restaurant hours ({table.restaurant.opening_time} to {table.restaurant.closing_time}).")

        # Check for overlapping bookings on the same tables
        for table in self.tables.all():
            overlapping_bookings = Booking.objects.filter(
                tables=table,
                booking_date=self.booking_date,
                start_time__lt=self.end_time,
                end_time__gt=self.start_time
            ).exclude(pk=self.pk)

            if overlapping_bookings.exists():
                raise ValidationError(f"Table {table.table_number} is already booked during this time slot.")

    @staticmethod
    def generate_booking_reference():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def save(self, *args, **kwargs):
        if not self.booking_reference:
            self.booking_reference = Booking.generate_booking_reference()
        super().save(*args, **kwargs)

    def cancel(self):
        """Cancels the booking if it's at least 2 hours before the booking time."""
        booking_datetime = datetime.combine(self.booking_date, self.start_time)
        now = timezone.now()
        
        # Check if the booking can be canceled (at least 2 hours before)
        if booking_datetime < now + timedelta(hours=2):
            raise ValidationError("You can only cancel your booking 2 hours in advance.")
        
        self.canceled = True
        self.save()
    
    def __str__(self):
        return f"Booking {self.booking_reference} for {self.customer_name} on {self.booking_date}"