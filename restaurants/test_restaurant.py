from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Restaurant


class RestaurantViewTests(TestCase):

    def setUp(self):
        """Set up test user"""
        self.user = User.objects.create_user(
            username='testuser', password='test123')

    def test_restaurant_list_view(self):
        """
        Set up test restaurant
        Test logged in user
        Test Filter by capacity (75)
        """
        Restaurant.objects.create(
            name='Restaurant One',
            address='123 test',
            description='great place to eat.',
            phone_number='1234567890',
            capacity=50,
            opening_time='09:00',
            closing_time='22:00',
            owner=self.user,
        )

        # Log in the user to access the view
        self.client.login(username='testuser', password='test123')

        response = self.client.get(reverse('restaurant_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Restaurant One')

    def test_filter_restaurant_by_capacity(self):
        # Create a Restaurant object
        Restaurant.objects.create(
            name='Restaurant One',
            address='123',
            description='Great food!',
            phone_number='123456789',
            capacity=75,
            opening_time='09:00',
            closing_time='22:00',
            owner=self.user,
        )

        # Log in the user to access the view
        self.client.login(username='testuser', password='test123')

        response = self.client.get(reverse('restaurant_list') + '?capacity=75')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Restaurant One')
