from django.contrib import admin
from .models import Restaurant, Table
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):
    list_display = ('name', 'capacity', 'opening_time', 'closing_time')
    search_fields = ['name']
    list_filter = ('name',)
    summernote_fields = ('description',)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'price', 'restaurant')
    list_filter = ('restaurant',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
