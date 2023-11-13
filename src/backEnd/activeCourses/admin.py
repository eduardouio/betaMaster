from simple_history.admin import SimpleHistoryAdmin
from django.contrib import admin

from .models import ActiveCourse


@admin.register(ActiveCourse)
class ActiveCourseModelAdmin(SimpleHistoryAdmin):
    list_display = (
        'study_plan',
        'student',
        'year',
        'period',

    )
    list_filter = (
        'state',
        'id_study_plan__name',
    )

    def study_plan(self, obj):
        return obj.id_study_plan.name

    def student(self, obj):
        return obj.id_student.first_name + ' ' + obj.id_student.last_name
