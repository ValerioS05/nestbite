from django.db import models

# Create your models here.
from django.db import models
from restaurants.models import Table

class Booking(models.Model):
    tables = models.ManyToManyField(Table, related_name='bookings')
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.customer_name} on {self.booking_date} at {self.start_time}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['booking_date', 'start_time', 'end_time'], name='unique_booking_time')
        ]