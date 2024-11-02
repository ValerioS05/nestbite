from django.db import models
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from restaurants.models import Table, Restaurant
import random
import string


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings'
    )
    tables = models.ManyToManyField(Table, related_name='bookings')
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    message = models.CharField(max_length=200, blank=True, null=True)
    booking_reference = models.CharField(
        max_length=10, unique=True, blank=True, null=True
    )
    canceled = models.BooleanField(default=False)

    def clean(self):
        """
        Validate booking details before saving the instance.

        Raises:
            ValidationError: If the booking time is in the past,
            less than two hours in advance, or more than twelve
            months in the future.
        """
        if self.start_time is None:
            raise ValidationError("Start time cannot be None.")
        if self.end_time is None:
            raise ValidationError("End time cannot be None.")
        booking_datetime_start = timezone.make_aware(
            datetime.combine(self.booking_date, self.start_time)
        )
        now = timezone.now()
        twelve_months_later = now + timedelta(days=365)

        if booking_datetime_start < now:
            raise ValidationError("Cannot book in the past.")
        if booking_datetime_start < now + timedelta(hours=2):
            raise ValidationError(
                "Bookings must be made at least 2 hours in advance."
            )
        if booking_datetime_start > twelve_months_later:
            raise ValidationError(
                "Bookings can only be made for up to 12 months in advance."
            )

    @staticmethod
    def generate_booking_reference():
        """
        Generate a unique booking reference consisting of uppercase letters
        and numbers.

        Returns:
            str:Randomly generated booking reference of 10 characters.
        """
        return ''.join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )

    def save(self, *args, **kwargs):
        """
        Save the booking instance, generating a booking reference if it
        doesn't already exist.
        """
        if not self.booking_reference:
            unique = False
            while not unique:
                reference = Booking.generate_booking_reference()
                if not Booking.objects.filter(booking_reference=reference).exists():
                    self.booking_reference = reference
                    unique = True
        super().save(*args, **kwargs)

    @property
    def total_price(self):
        return sum(table.price for table in self.tables.all())

    def cancel(self):
        """
        Cancel the booking if it is at least 2 hours before the booking time.

        Raises:
            ValidationError:When attempting to cancel in less than 2 hours
            of the booking time.
        """
        booking_datetime = timezone.make_aware(
            datetime.combine(self.booking_date, self.start_time)
        )
        now = timezone.now()

        if booking_datetime < now + timedelta(hours=2):
            raise ValidationError(
                "You can only cancel your booking 2 hours in advance."
            )

        self.canceled = True
        self.save()

    def __str__(self):
        return (
            f"Booking {self.booking_reference} for {self.customer_name} "
            f"on {self.booking_date}"
        )


class Review(models.Model):
    booking = models.ForeignKey(
        'Booking', on_delete=models.SET_NULL, null=True, related_name='reviews'
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='reviews'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return (
            f"{self.user.username} - {self.rating} Stars for Booking "
            f"{self.booking.booking_reference if self.booking else 'N/A'}"
        )
