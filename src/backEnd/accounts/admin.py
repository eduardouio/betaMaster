from typing import Any
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUserModel, PersonalReferences, BankAccount
from .forms import CustomCreationForm, UserForm


class CustomUserModelAdmin(UserAdmin):
    form = UserForm
    add_form = CustomCreationForm
    model = CustomUserModel

    fieldsets = (
        ('Basico', {'fields': ('email', 'password', 'role', 'is_active', 'is_aproved', 'is_confirmed_mail')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'dni_number', 'date_of_birth', 'phone', 'address', 'country', 'state', 'city', 'canton', 'presentation', 'cv', 'notes')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    list_display = (
        'email',
        'first_name',
        'last_name',
        'role',
        'dni_number',
        'is_active',
        'is_aproved',
        'is_confirmed_mail',
    )

    list_filter = (
        'role',
        'is_active',
    )

    ordering = ('email', 'role')

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.form = CustomCreationForm
        else:
            self.form = UserForm

        return super().get_form(request, obj, **kwargs)


@admin.register(PersonalReferences)
class PersonalReferencesAdmin(SimpleHistoryAdmin):
    list_display = (
        'id_reference',
        'id_user',
        'type',
        'enterprise',
        'name_contact',
        'phone_contact',
        'email_contact',
        'relationship',
        'is_verified',
        'verification_date',
        'verification_by',
    )

    list_filter = (
        'type',
        'relationship',
        'is_verified',
    )


@admin.register(BankAccount)
class BankAccountAdmin(SimpleHistoryAdmin):
    list_display = (
        'owner_name',
        'bank_name',
        'type_account',
        'is_active'
    )


admin.site.register(CustomUserModel, CustomUserModelAdmin)
