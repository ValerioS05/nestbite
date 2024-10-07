from django import forms
from .models import Booking
from restaurants.models import Table

class BookingForm(forms.ModelForm):
    tables = forms.ModelMultipleChoiceField(
        queryset=Table.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Booking
        fields = ['customer_name', 'booking_date', 'start_time', 'end_time', 'message', 'tables']