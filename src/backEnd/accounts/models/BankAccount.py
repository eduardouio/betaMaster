from django.db import models
from common import BaseModel
from .CustomUserModel import CustomUserModel

TYPE_ACCOUNT = (
    ('AHORROS', 'AHORROS'),
    ('CORRIENTE', 'CORRIENTE'),
    ('OTRO', 'OTRO'),
)


class BankAccount(BaseModel):
    id_bank = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(
        CustomUserModel,
        on_delete=models.RESTRICT
    )
    nro_account = models.CharField(
        'Número de Cuenta',
        max_length=30
    )
    bank_name = models.CharField(
        'Nombre Banco',
        max_length=50
    )
    type_account = models.CharField(
        'Tipo Cuenta',
        max_length=50,
        choices=TYPE_ACCOUNT
    )
    email_notify = models.EmailField(
        'Correo Notificación',
        max_length=100
    )
    owner_name = models.CharField(
        'Nombre Titular',
        max_length=100
    )
    owner_dni = models.CharField(
        'Cédula Titular',
        max_length=50
    )
    is_verified = models.BooleanField(
        'Cuenta Verificada',
        default=False
    )
