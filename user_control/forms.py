from django import forms
from user_control.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    display_name = forms.CharField(help_text="What should we call you?")
    class Meta:
        model = UserProfile
        fields = ['display_name']#Hiding the can_direct_edit 
