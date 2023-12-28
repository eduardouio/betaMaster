from django import forms
from accounts.models import CustomUserModel as UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = (
            'email',
            'role',
            'country',
            'state',
            'city',
            'canton',
            'date_of_birth',
            'address',
            'phone',
            'presentation',
            'cv',
            'is_aproved',
            'is_confirmed_mail',
            'is_active',
            'notes'
        )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provincia'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'canton': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantón'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de nacimiento'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'presentation': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Presentación'}),
            'cv': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'CV'}),
            'is_aproved': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Aprobado'}),
            'is_confirmed_mail': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Confirmado'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Activo'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notas'}),
        }
