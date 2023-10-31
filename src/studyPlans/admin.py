from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import StudyPlan, StudyPlanDetail


@admin.register(StudyPlan)
class StudyPlanAdmin(SimpleHistoryAdmin):
    list_display = (
        'name',
        'coordinator',
        'date_start',
        'due_date',
        'is_active',
        'created_at',
    )


@admin.register(StudyPlanDetail)
class StudyPlanDetailAdmin(SimpleHistoryAdmin):
    pass
