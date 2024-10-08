# Generated by Django 4.2.15 on 2024-09-09 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('phone_number', models.CharField(max_length=25)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('capacity', models.PositiveIntegerField()),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
