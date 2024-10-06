# Generated by Django 4.2.15 on 2024-10-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_alter_restaurant_options_alter_table_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
