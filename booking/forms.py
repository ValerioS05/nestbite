from django import forms
# Import the forms module from Django
from .models import Booking, Review
# Import the Booking model from the current app
from restaurants.models import Table, Restaurant
# Import the Table and Restaurant models from the restaurants app


# Define form based on the Booking model
class BookingForm(forms.ModelForm):
    tables = forms.ModelMultipleChoiceField(
        queryset=Table.objects.none(),
        required=True,
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Booking  # specify which model
        fields = ['tables', 'customer_name', 'booking_date',
                  'start_time', 'end_time', 'message']

    def __init__(self, *args, **kwargs):
        restaurant_id = kwargs.pop('restaurant_id', None)
        # Get the restaurant id from keywords
        super().__init__(*args, **kwargs)

        # Filter tables based on the selected restaurant
        if restaurant_id:  # Check if an id was provided
            self.fields['tables'].queryset = Table.objects.filter(
                restaurant_id=restaurant_id
            )  # Filter tables of specified id

            self.fields['tables'].choices = [
                (table.id, f"""
                    Table {table.table_number} (Max: {table.capacity})
                    - £{table.price:.2f}""")
                # Display the table and price
                for table in self.fields['tables'].queryset
            ]

            # Fetch the restaurant to get opening and closing hours
            restaurant = Restaurant.objects.get(id=restaurant_id)
            opening_time = restaurant.opening_time
            closing_time = restaurant.closing_time

            # Set widgets for date
            self.fields['booking_date'].widget = forms.DateInput(
                attrs={'type': 'date'}
            )  # Date picker

            # Set initial value and attributes for start_time
            self.fields['start_time'].widget = forms.TimeInput(
                attrs={
                    'type': 'time',
                    'min': opening_time,
                    'max': (closing_time.hour - 1)
                }
            )

            self.fields['end_time'].widget = forms.TimeInput(
                attrs={
                    'type': 'time',
                    'min': f"{(opening_time.hour + 1)}:00",
                    'max': closing_time
                }
            )


# Define form based on the Review model
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'message']
        widgets = {
            'rating': forms.RadioSelect(
                choices=[
                    (1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'),
                    (4, '4 Stars'), (5, '5 Stars')
                ]
            ),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Leave a message (optional)', 'rows': 4
                }
            ),
        }
