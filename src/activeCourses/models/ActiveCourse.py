from django.db import models
from accounts.models import CustomUserModel
from schools.models import School
from studyPlans.models import StudyPlan
from common import BaseModel


STATES = (
    ('POR INICIAR', 'POR INICIAR'),
    ('EN PROCESO', 'EN PROCESO'),
    ('FINALIZADO', 'FINALIZADO'),
)

# SE REGISTRAN UN SOLO PROFESOR PARA UN CURSO?
# Como se majena el tema de los profesores?
# como se manejan a los estudiantes, entiendo que cada uno tiene un plan de
# estudio
# es un solo profesor o varios?


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
    id_teacher = models.ForeignKey(
        CustomUserModel,
        on_delete=models.RESTRICT
    )
    id_student = models.ForeignKey(
        CustomUserModel,
        on_delete=models.RESTRICT
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
    calification = models.DecimalField(
        'Calificación',
        max_digits=5,
        decimal_places=2,
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
