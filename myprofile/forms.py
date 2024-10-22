from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    """ 
    Form based on default User model
    and allows users to update their details. 
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ContactForm(forms.Form):
    """ Simple CharField as widget(textarea) for the user to insert their message. """
    message = forms.CharField(widget=forms.Textarea, label="Your Message")

