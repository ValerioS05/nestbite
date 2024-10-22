from django import forms
from .models import Booking, Review
from restaurants.models import Table, Restaurant


class BookingForm(forms.ModelForm):
    """
    A form for creating and managing restaurant table bookings.

    The form is based on the Booking model and allows users to select tables,
    provide customer details, and specify booking date and times.
    The tables are filtered based on the selected restaurant, and the form automatically
    sets the time input fields according to the restaurant opening and closing.

    Attributes:
        tables (ModelMultipleChoiceField): A checkbox field that allows multiple table
        selection, filtered by the specified restaurant.
    """
    tables = forms.ModelMultipleChoiceField(
        queryset=Table.objects.none(),
        required=True,
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        """ Specifies the model and the fields to be included in the form. """
        model = Booking
        fields = ['tables', 'customer_name', 'booking_date',
                  'start_time', 'end_time', 'message']

    def __init__(self, *args, **kwargs):
        """
        Initializes the BookingForm and filters the available tables based on the restaurant.
        Sets date and time picker for booking date and times.
        """
        restaurant_id = kwargs.pop('restaurant_id', None)
        super().__init__(*args, **kwargs)

        if restaurant_id:
            self.fields['tables'].queryset = Table.objects.filter(
                restaurant_id=restaurant_id
            )

            self.fields['tables'].choices = [
                (table.id, f"""
                    Table {table.table_number} (Max: {table.capacity})
                    - £{table.price:.2f}""")
                for table in self.fields['tables'].queryset
            ]

            restaurant = Restaurant.objects.get(id=restaurant_id)
            opening_time = restaurant.opening_time
            closing_time = restaurant.closing_time

            self.fields['booking_date'].widget = forms.DateInput(
                attrs={'type': 'date'}
            )

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


class ReviewForm(forms.ModelForm):
    """
    This form is based on the Review model and allows users to provide a rating (1 to 5)
    and leave an optional message.
    """
    class Meta:
        """ custom widgets for the rating and message fields. """
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
