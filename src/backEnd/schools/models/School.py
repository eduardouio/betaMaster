from django.db import models
from accounts.models import CustomUserModel
from common import BaseModel

OFFERED_SERVICES = (
    ('INICIAL', 'EDUACIÓN INICIAL'),
    ('BASICA', 'EDUACIÓN BÁSICA'),
    ('BGU', 'BACHILLERATO GENERAL UNIFICADO'),
    ('TECNICO', 'BACHILLERATO TÉCNICO'),
    ('OTRO', 'OTRO')
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
    ami_code = models.CharField(
        'CODIGO AMI',
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
        null=True,
        default=None
    )
    presentation_document = models.FileField(
        'Presentación',
        upload_to='schools/',
        blank=True,
        null=True,
        default=None
    )
    description = models.TextField(
        'Descripción',
        blank=True,
        null=True,
        default=None
    )
    offer_services = models.CharField(
        'Servicios Ofrecidos',
        max_length=250,
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
