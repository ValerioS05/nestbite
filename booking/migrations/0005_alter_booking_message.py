# Generated by Django 4.2.15 on 2024-10-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='message',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]