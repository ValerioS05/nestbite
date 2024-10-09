from django import forms # Import the forms module from Django
from .models import Booking # Import the Booking model from the current app
from restaurants.models import Table # Import the Table model from the restaurants app

# Define form based on the Booking model
class BookingForm(forms.ModelForm):
    tables = forms.ModelMultipleChoiceField(queryset=Table.objects.none(), required=True)

    class Meta:
        model = Booking  # specify which model
        fields = ['tables', 'customer_name', 'booking_date', 'start_time', 'end_time', 'message'] # Fields included in the form

    def __init__(self, *args, **kwargs):
        restaurant_id = kwargs.pop('restaurant_id', None) # Get the restaurant id from keywords
        super().__init__(*args, **kwargs)

        # Filter tables based on the selected restaurant
        if restaurant_id: # Check if an id was provided
            self.fields['tables'].queryset = Table.objects.filter(restaurant_id=restaurant_id) # Filter tables of specified id

            table_choices = [
                (table.id, f"{table} - £{table.price:.2f}")  # Display the table and price
                for table in self.fields['tables'].queryset
            ]
            self.fields['tables'].choices = table_choices