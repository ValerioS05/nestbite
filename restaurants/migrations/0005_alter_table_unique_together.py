# Generated by Django 4.2.15 on 2024-10-06 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_table_price'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='table',
            unique_together={('restaurant', 'table_number')},
        ),
    ]
