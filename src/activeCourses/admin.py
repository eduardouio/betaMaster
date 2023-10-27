from simple_history.admin import SimpleHistoryAdmin
from django.contrib import admin

from .models import ActiveCourse


@admin.register(ActiveCourse)
class ActiveCourseModelAdmin(SimpleHistoryAdmin):
    list_display = (
        'year',
        'period',
        'level',
        'state',
        'calification',
        'description',
    )
