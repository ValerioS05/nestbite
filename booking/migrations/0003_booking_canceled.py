# Generated by Django 4.2.15 on 2024-10-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_booking_unique_booking_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='canceled',
            field=models.BooleanField(default=False),
        ),
    ]
