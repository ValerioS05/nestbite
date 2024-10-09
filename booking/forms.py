from django import forms # Import the forms module from Django
from .models import Booking # Import the Booking model from the current app
from restaurants.models import Table, Restaurant  # Import the Table and Restaurant models from the restaurants app

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

            # Fetch the restaurant to get opening and closing hours
            restaurant = Restaurant.objects.get(id=restaurant_id)
            opening_time = restaurant.opening_time
            closing_time = restaurant.closing_time
            
            # Set widgets for date
            self.fields['booking_date'].widget = forms.DateInput(attrs={'type': 'date'})  # Date picker

            # Set initial value and attributes for start_time
            self.fields['start_time'].widget = forms.TimeInput(attrs={'type': 'time', 'min': opening_time, 'max': (closing_time.hour - 1)})
            self.fields['end_time'].widget = forms.TimeInput(attrs={'type': 'time', 'min': f"{(opening_time.hour + 1)}:00", 'max': closing_time})