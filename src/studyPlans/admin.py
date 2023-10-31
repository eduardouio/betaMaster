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
    list_display = (
        'studyplan',
        'asignature',
        'level',
        'credits',
        'minimun_score',
        'is_active',
    )

    list_filter = (
        'id_study_plan__name',
        'level',
    )

    def studyplan(self, obj):
        return obj.id_study_plan.name
    studyplan.short_description = 'Plan de Estudio'
