from django import forms
from .models import Booking
from restaurants.models import Table

class BookingForm(forms.ModelForm):
    tables = forms.ModelMultipleChoiceField(queryset=Table.objects.none(), required=True)  # Allow selection of multiple tables

    class Meta:
        model = Booking
        fields = ['tables', 'customer_name', 'booking_date', 'start_time', 'end_time', 'message']

    def __init__(self, *args, **kwargs):
        restaurant_id = kwargs.pop('restaurant_id', None)
        super().__init__(*args, **kwargs)

        # Filter tables based on the selected restaurant
        if restaurant_id:
            self.fields['tables'].queryset = Table.objects.filter(restaurant_id=restaurant_id)
