from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import CustomUserModel


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

admin.site.site_header = 'HomeSchooling'
