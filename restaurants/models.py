from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    description = models.TextField()
    phone_number = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    capacity = models.PositiveIntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT
    )