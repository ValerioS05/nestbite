from django.contrib import admin
from .models import Restaurant,Table
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):

    list_display = ('name', 'capacity', 'opening_time', 'closing_time')
    search_fields = ['name']
    list_filter = ('name',)
    summernote_fields = ('description',)
# Register your models here.



admin.site.register(Table)