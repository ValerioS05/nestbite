# Generated by Django 4.2.15 on 2024-09-23 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ['table_number', 'restaurant']},
        ),
    ]