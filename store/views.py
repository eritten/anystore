from django.shortcuts import render
from .forms import UserRegistrationForm, ProfileForm
import requests
from django.conf import settings
# importing make_password
from django.contrib.auth.hashers import make_password
from django.contrib import messages



# Create your views here.

# home page
def home(request):
    return render(request, 'home.html')

# user registration
def signup(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # saving the user
            user = form.save(commit=False)
            # hashing the password
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        return render(request, 'signup.html', {'form': form})
    return render(request, 'signup.html', {'form': form})

# user profile
def profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # saving the profile
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile created successfully')
            return redirect('profile')
        return render(request, 'profile.html', {'form': form})
    return render(request, 'profile.html', {'form': form})

