from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    description = models.TextField()
    phone_number = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)                       # automatic time stamp when created
    capacity = models.PositiveIntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT                                      # Restaurant protected from delete (connected to User)
    )

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ['name']                                                   # ordering by name

class Table(models.Model):
    restaurant = models.ForeignKey(                                           # related to Restaurant model
        Restaurant, on_delete=models.CASCADE, related_name='tables'           # deleted if restaurant is deleted
        )
    table_number = models.CharField(max_length=3)
    capacity = models.IntegerField()
    
    def __str__(self):
        return f"Table {self.table_number} (Max:{self.capacity}) at {self.restaurant} "

    class Meta:
        ordering = ['table_number', 'restaurant']

