from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileForm
from django.contrib.auth.models import User

@login_required
def profile_view(request):
    return render(request, 'profile/profile.html', {'user': request.user})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if User.objects.filter(username=username).exclude(pk=request.user.pk).exists():
                form.add_error('username', "This username is already in use.")
            if User.objects.filter(email=email).exclude(pk=request.user.pk).exists():
                form.add_error('email', "This email is already in use.")
            if not form.errors:
                form.save()
                messages.success(request, 'Your profile has been updated successfully!')
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'profile/update_profile.html', {'form': form})
