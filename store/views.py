from django.shortcuts import render, redirect
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
        return render(request, 'registration/signup.html', {'form': form})
    return render(request, 'registration/signup.html', {'form': form})

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



def privacy(request):
    return render(request, "privacy.html")
def terms(request):
    return render(request, "terms.html")


# function base base view to make user account not active using is_active attribute
def deactivate(request):
    user = request.user
    user.email_user(f"{user.username.capitalize()}, your account has been disabled", """We  are sorry to see you go! \r Please email us any questions/concerns you may have at below email: support@anystoreweb.com. Kind regards, 
                    
                    Anystore Team. \r
                    https://www.anystoreweb.com \r You can also download it from Play Store and App Store.""")
    user.is_active = False
    user.save()
    messages.success(request, 'Account deactivated successfully')
    return redirect('login')

