from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import UniqueConstraint


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

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['name']


class Table(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='tables'
    )
    table_number = models.CharField(max_length=3)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        current_total_capacity = sum(
            table.capacity for table in self.restaurant.tables.all()
            )
        if self.capacity <= 0:
            raise ValidationError("Table capacity must be a positive integer.")
        if current_total_capacity + self.capacity > self.restaurant.capacity:
            raise ValidationError(
                f"""Cannot add table. Adding this table
                would exceed the restaurant's total capacity of
                {self.restaurant.capacity}."""
            )
        if self.restaurant.tables.filter(
                table_number=self.table_number).exists():
            raise ValidationError(
                f"""Table number '{self.table_number}'
                already exists in this restaurant."""
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"""Table {self.table_number}
        (Max: {self.capacity}) at {self.restaurant}"""

    class Meta:
        ordering = ['table_number', 'restaurant']
        constraints = [
            UniqueConstraint(fields=[
                'restaurant',
                'table_number'
                ], name='unique_table_number_per_restaurant'),
        ]
