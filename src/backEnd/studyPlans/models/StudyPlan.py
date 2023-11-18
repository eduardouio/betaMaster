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
        on_delete=models.RESTRICT
    )
    date_start = models.DateTimeField(
        'Fecha Inicio',
        default=None,
        blank=True,
        null=True
    )
    document = models.FileField(
        'Documento Plan Estudio',
        upload_to='studyPlans/',
        blank=True,
        null=True,
        default=None
    )
    due_date = models.DateTimeField(
        'Vencimiento',
        blank=True,
        null=True,
        default=None
    )
