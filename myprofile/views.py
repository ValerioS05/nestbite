from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, ProfileForm
from django.contrib.auth.models import User


@login_required
def profile_view(request):
    """ Render the profile view for the logged user. """
    return render(request, 'profile/profile.html', {'user': request.user})


@login_required
def profile_edit(request):
    """
    Allow the logged user to edit their profile information (username/email).
    Validateing the uniqueness of the username/email.

    Args:
        request (HttpRequest): The HTTP request. If POST attempts to 
        update the profile. Otherwise, renders the form with the current user details.

    Returns:
        HttpResponse: Redirects to the profile page if successful, or renders 
        the form with validation errors if any.
    """
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if User.objects.filter(username=username).exclude(
                pk=request.user.pk
            ).exists():
                form.add_error('username', "This username is already in use.")
            if User.objects.filter(email=email).exclude(
                pk=request.user.pk
            ).exists():
                form.add_error('email', "This email is already in use.")
            if not form.errors:
                form.save()
                messages.success(request,
                                 'Your profile has been updated successfully!')
                return redirect('profile')
            else:
                messages.error(request, 'There was an error! Try again.')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'profile/update_profile.html', {'form': form})


@login_required
def contact_us(request):
    """
    Handle the form submission for logged users.
    Sends an email to the site admin containing the user's message.

    Args:
        request (HttpRequest): The HTTP request. If POST, processes 
        the form submission and sends the message. otherwise, renders 
        an empty form.

    Returns:
        HttpResponse: Redirects to the Contact Us page if the message 
        was successfully sent or re-renders the form with an error message 
        in case of any.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            username = request.user.username
            email = request.user.email
            email_subject = f'Contact us form submission from {username}'
            email_body = (
                f"Username: {username}\nEmail: {email}\nMessage:\n{message}"
            )

            try:
                send_mail(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    ['nestbite@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request,
                                 'Your message has been sent successfully!')
                return redirect('contact_us')
            except Exception as e:
                messages.error(request,
                               'There was an error sending the message. '
                               'Please try again.')
    else:
        form = ContactForm()

    return render(request, 'profile/contact_us.html', {'form': form})
