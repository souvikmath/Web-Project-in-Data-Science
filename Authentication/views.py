from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import cache_control
from .forms import RegisterForm, LoginForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Optionally log in the user automatically
            messages.success(request, 'Registered successfully!')
            return redirect('login')  # Redirect to login page after registration
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, user_id=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile')  # Redirect to the profile or dashboard page
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        # Handle form submission to update the profile
        time_zone = request.POST.get('time_zone')
        location = request.POST.get('location')

        # Update the user's profile information
        request.user.time_zone = time_zone
        request.user.location = location
        request.user.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')  # Redirect to the same profile page after updating
    # If it's a GET request, render the profile form
    return render(request, 'profile.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to login page after logging out
