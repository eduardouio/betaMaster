from django.db import models
from accounts.models import CustomUserModel
from schools.models import School
from studyPlans.models import StudyPlan
from common import BaseModel


STATES = (
    ('por iniciar', 'POR INICIAR'),
    ('en proceso', 'EN PROCESO'),
    ('finalizado', 'FINALIZADO'),
)


class ActiveCourse(BaseModel):
    id_active_courses = models.AutoField(primary_key=True)
    id_school = models.ForeignKey(
        School,
        on_delete=models.RESTRICT
    )
    id_study_plan = models.ForeignKey(
        StudyPlan,
        on_delete=models.RESTRICT
    )
    student = models.ForeignKey(
        CustomUserModel,
        related_name='student',
        on_delete=models.RESTRICT
    )
    teacher = models.ManyToManyField(
        CustomUserModel,
        related_name='teacher',
    )
    year = models.PositiveIntegerField(
        'Año',
        default=0
    )
    period = models.CharField(
        'Periodo',
        max_length=60,
    )
    level = models.CharField(
        'Nivel',
        max_length=60,
    )
    state = models.CharField(
        'Estado',
        max_length=60,
        choices=STATES,
        default='POR INICIAR',
    )
    calification = models.FloatField(
        'Calificación',
        blank=True,
        null=True,
        default=None,
    )
    description = models.TextField(
        'Descripción',
        blank=True,
        null=True,
        default=None,
    )
