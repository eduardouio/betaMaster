from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from schools.models import School


@admin.register(School)
class SchoolAdmin(SimpleHistoryAdmin):
    list_display = (
        'name',
        'city',
        'state',
        'email',
        'ami_code',
        'type_school',
    )
    search_fields = (
        'name',
        'email',
        'ami_code',
    )
    list_filter = (
        'name',
        'email',
    )
