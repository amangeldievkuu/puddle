from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'w-full py-4 px-6 rounded-xl',
        'id': 'username'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password',
        'class': 'w-full py-4 px-6 rounded-xl',
        'id': 'password',
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'username',
        'class': 'w-full py-4 px-6 rounded-xl',
        'id': 'username',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'email',
        'class': 'w-full py-4 px-6 rounded-xl',
        'id': 'email',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password',
        'class': 'w-full py-4 px-6 rounded-xl',
        'id': 'password1',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs = {
        'placeholder': 'confirm password',
        'class': 'w-full py-4 px-6 rounded-xl',
        'id': 'password2',
    }))

