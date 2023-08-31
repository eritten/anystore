# importing user model
from django.contrib.auth.models import User
# importing forms
from django import forms
from .models import Profile
import re
# creating a form for user registration
class UserRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),
        
        
        }
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password does not match')
        return cd['password2']


#validating password field. password should be at least 8 characters long and should contain at least one digit and one special character
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Password should be at least 8 characters long')
        if not re.search('[0-9]', password):
            raise forms.ValidationError('Password should contain at least one digit')
        if not re.search('[^A-Za-z0-9]', password):
            raise forms.ValidationError('Password should contain at least one special character')
        return password
    

    # cleaning username field
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username
    
    # cleaning email field
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email
    
    
# creating a form for user profile
# it has one to one relationship with user model. image is optional
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
        widgets = {
            'image': forms.FileInput(attrs={'class':'form-control'}),
        }
        
    # cleaning image field. the image size should be less than 3MB
    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            if image.size > 3*1024*1024:
                raise forms.ValidationError('Image size should be less than 3MB')
        return image
    
