from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Booking, Table
from django.contrib.auth.models import User
from restaurants.models import Restaurant


class BookingTests(TestCase):
    """Set up test user/restaurant/table"""
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            address='123',
            description='great place to eat.',
            phone_number='1234567890',
            capacity=20,
            opening_time='10:00',
            closing_time='22:00',
            owner=self.user,
        )

        self.table = Table.objects.create(
            restaurant=self.restaurant,
            table_number='1',
            capacity=4,
            price=10.00
        )

    def test_create_booking(self):
        """Test booking creation table/user/time constraints."""
        self.client.login(username='testuser', password='testpass')

        start_time = (timezone.now() + timedelta(hours=2, minutes=1)).time()
        end_time = (timezone.now() + timedelta(hours=3, minutes=1)).time()

        booking_data = {
            'customer_name': 'Test User',
            'customer_email': 'test@example.com',
            'booking_date': timezone.now().date(),
            'start_time': start_time,
            'end_time': end_time,
            'tables': [self.table.id],
            'user': self.user.id,
        }

        response = self.client.post(
            reverse('create_booking', args=[self.restaurant.id]),
            booking_data
        )

        print("Response status code:", response.status_code)
        print("Response content:", response.content)

        self.assertEqual(Booking.objects.count(), 1, "No booking was created")
        booking = Booking.objects.first()
        self.assertEqual(booking.customer_name, 'Test User')
        self.assertEqual(booking.user, self.user)
        self.assertIn(self.table, booking.tables.all())
