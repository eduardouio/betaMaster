from django import forms
from django.contrib.auth.forms import UserChangeForm
from accounts.models import CustomUserModel as UserModel


class CustomChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('email', 'role', )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }
