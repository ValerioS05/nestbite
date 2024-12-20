from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


class BookingAdmin(SummernoteModelAdmin):
    list_display = ('customer_name', 'booking_date', 'start_time', 'end_time','canceled')
    search_fields = ['customer_name', 'customer_email']
    list_filter = ('booking_date',)
    ordering = ('booking_date', 'start_time')
    date_hierarchy = 'booking_date'
    summernote_fields = ('message',)


admin.site.register(Booking, BookingAdmin)
