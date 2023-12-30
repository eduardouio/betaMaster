from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUserModel
from accounts.models import PersonalReferences, BankAccount
from accounts.forms import CustomCreationForm, CustomChangeForm


class CustomUserModelAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomChangeForm

    model = CustomUserModel

    fieldsets = (
        ('Basico', {
            'fields': (
                'email', 'role', 'password', 'is_active', 'is_aproved',
                'is_confirmed_mail'
            )
        }
        ),
        ('Información Personal', {
            'fields': (
                'first_name', 'last_name', 'dni_number', 'date_of_birth',
                'phone', 'address', 'country', 'state', 'city', 'canton',
                'geolocation', 'presentation', 'cv', 'notes'
            )
        }
        ),
        ('Permisos', {
            'fields': (
                'is_staff', 'is_superuser', 'groups', 'user_permissions'
            )
        }
        ),
        ('Otros', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        ('Básico', {
            'classes': ('wide',),
            'fields': (
                'email', 'role', 'password1', 'password2',
                'is_staff', 'is_active'
            )
        }
        ),
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

    ordering = ('email',)


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
