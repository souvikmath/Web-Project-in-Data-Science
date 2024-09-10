from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    user_id = forms.CharField(max_length=100, help_text='Required.')
    email = forms.EmailField(help_text='Required.')

    class Meta:
        model = CustomUser
        fields = ['user_id', 'email', 'password1', 'password2']
        # Include 'user_id' and 'email' in the fields list to ensure they are displayed in the form

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
