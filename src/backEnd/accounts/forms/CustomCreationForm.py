from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUserModel as UserModel


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'role', 'password1', 'password2', )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }
