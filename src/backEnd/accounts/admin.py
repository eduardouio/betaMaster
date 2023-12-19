from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import CustomUserModel, PersonalReferences, BankAccount


@admin.register(CustomUserModel)
class CustomUserModelAdmin(SimpleHistoryAdmin):
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
        'tipe_account',
        'is_active'
    )


admin.site.site_header = 'HomeSchooling'
