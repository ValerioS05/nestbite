from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail
from .forms import ProfileForm, ContactForm


class ProfileViewTests(TestCase):

    def setUp(self):
        """ Set up test user"""
        self.user = User.objects.create_user(
            username='testuser', password='test123'
            )

    def test_profile_edit_valid_data(self):
        """Test user can  update their profile successfully."""
        self.client.login(username='testuser', password='test123')
        response = self.client.post(reverse('profile_edit'), {
            'username': 'username',
            'email': 'email@test.com'
        })
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.username, 'username')
        self.assertEqual(self.user.email, 'email@test.com')

    def test_contact_us_valid_data(self):
        """Test user can send a message with the contact form."""
        self.client.login(username='testuser', password='test123')
        response = self.client.post(reverse('contact_us'), {
            'message': 'Hello!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Contact us form submission', mail.outbox[0].subject)
