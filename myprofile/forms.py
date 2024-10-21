from django import forms
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label="Your Message")

