from django.db import models
from accounts.models import CustomUserModel
from common import BaseModel

TYPE_SCHOOL = (
    ('PUBLICO', 'PUBLICO'),
    ('PRIVADO', 'PRIVADO')
)


class School(BaseModel):
    id_school = models.AutoField(primary_key=True)
    name = models.CharField(
        'Nombre Colegio',
        max_length=100,
        unique=True
    )
    email = models.CharField(
        'Correo',
        max_length=100
    )
    dni_collegue = models.CharField(
        'Ruc Colegio',
        max_length=50
    )
    state = models.CharField(
        'Provincia',
        max_length=100
    )
    city = models.CharField(
        'Ciudad',
        max_length=100
    )
    address = models.CharField(
        'Dirección',
        max_length=100,
        blank=True,
        null=True,
        default=None
    )
    geolocation = models.CharField(
        'Geolocalización',
        max_length=500,
        blank=True,
        null=True,
        default=None
    )
    phone = models.CharField(
        'Teléfono',
        max_length=50,
        blank=True,
        null=True,
        default=None
    )
    website = models.URLField(
        'Sitio Web',
        max_length=100,
        blank=True,
        null=True
    )
    logo = models.ImageField(
        'Logo',
        upload_to='school/logos/',
        blank=True,
        null=True
    )
    description = models.TextField(
        'Descripción',
        blank=True,
        null=True,
        default=None
    )
    type_school = models.CharField(
        'Tipo Colegio',
        max_length=50,
        blank=True,
        null=True,
        default=None
    )
    id_owner = models.ForeignKey(
        CustomUserModel,
        on_delete=models.RESTRICT
    )

    def __str__(self) -> str:
        return self.name
