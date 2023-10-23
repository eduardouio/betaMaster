from django.db import models
from common import BaseModel
from studyPlans.models import StudyPlan

class StudyPlanDetail(BaseModel):
    id_study_plan_detail = models.AutoField(primary_key=True)
    id_study_plan = models.ForeignKey(StudyPlan)
    asignature = models.CharField(
        'Asignatura',
        max_length=60,
    )
    level = models.PositiveIntegerField(
        'Nivel',
        default=0
    )
    credits = models.PositiveIntegerField(
        'Créditos',
        default=0
    )
    minimun_score = models.PositiveIntegerField(
        'Puntuación Mínima',
        blank=True,
        null=True
        default=0,
    )
    description = models.TextField(
        'Descripción',
        blank=True,
        null=True,
        default=None,
    )
