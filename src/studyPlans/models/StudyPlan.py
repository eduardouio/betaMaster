from django.db import models
from accounts.models import CustomUserModel
from common import BaseModel


class StudyPlan(BaseModel):
    id_study_plan = models.AutoField(primary_key=True)
    name = models.CharField(
        'Nombre',
        max_length=120,
        unique=True
    )
    coordinator = models.ForeignKey(
        CustomUserModel,
    )
    date_start = models.DateTimeField(
        'Fecha Inicio',
        auto_now_add=True,
        default=None,
        blank=True,
        null=True
    )
    due_date = models.DateTimeField(
        'Vencimiento',
        blank=True,
        null=True,
        default=None
    )
