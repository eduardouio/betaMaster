from django.db import models
from common import BaseModel
from accounts.models import CustomUserModel

TYPE_SUBSCRIPTION = (
    ('SCHOOL', 'SCHOOL'),
    ('TEACHER', 'TEACHER'),
    ('STUDENT', 'STUDENT'),
    ('OTHER', 'OTHER'),
)


class Subscription(BaseModel):
    id_subscription = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(
        CustomUserModel,
        on_delete=models.RESTRICT
    )
    date_start = models.DateTimeField(
        'Fecha Inicio',
        blank=True,
        null=True,
        default=None
    )
    date_end = models.DateTimeField(
        'Fecha Fin',
        blank=True,
        null=True,
        default=None
    )
    type_subscription = models.CharField(
        'Tipo de Suscripción',
        max_length=60,
        choices=TYPE_SUBSCRIPTION,
        default='OTHER',
    )
    cost = models.DecimalField(
        'Valor',
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        default=None,
    )
