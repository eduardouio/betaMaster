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
        'dni_collegue',
        'type_school',
    )
    search_fields = (
        'name',
        'email',
        'dni_collegue',
    )
    list_filter = (
        'name',
        'email',
        'dni_collegue',
    )
