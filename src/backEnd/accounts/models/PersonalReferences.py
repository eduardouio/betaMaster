from django.db import models
from common import BaseModel
from .CustomUserModel import CustomUserModel

TYPE_REFERENCES = (
    ('PERSONAL', 'PERSONAL'),
    ('PROFESIONAL', 'PROFESIONAL'),
)

TYPE_RELATIONSHIP = (
    ('FAMILIAR', 'FAMILIAR'),
    ('JEFE', 'JEFE INMEDIATO'),
    ('AMIGO', 'COMPAÑERO DE TRABAJO'),
    ('OTRO', 'OTRO'),
)


class PersonalReferences(BaseModel):
    id_reference = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(
        CustomUserModel,
        on_delete=models.CASCADE
    )
    type = models.CharField(
        'Tipo de Referencia',
        max_length=100,
        choices=TYPE_REFERENCES,
    )
    document = models.FileField(
        'Documento',
        upload_to='references/',
        blank=True,
        null=True,
        default=None
    )
    enterprise = models.CharField(
        'Empresa',
        max_length=100
    )
    start_date = models.DateField(
        'Fecha de Inicio',
        blank=True,
        null=True,
        default=None,
    )
    end_date = models.DateField(
        'Fecha de Fin',
        blank=True,
        null=True,
        default=None,
    )
    name_contact = models.CharField(
        'Nombre de Contacto',
        max_length=100
    )
    phone_contact = models.CharField(
        'Teléfono de Contacto',
        max_length=40,
        blank=True,
        null=True,
    )
    email_contact = models.CharField(
        'Correo de Contacto',
        max_length=100
    )
    relationship = models.CharField(
        'Relación',
        max_length=100,
        choices=TYPE_RELATIONSHIP,
    )
    is_verified = models.BooleanField(
        'verificado?',
        default=False
    )
    verification_date = models.DateTimeField(
        'Fecha de Verificación',
        blank=True,
        null=True,
        default=None,
    )
    verification_by = models.PositiveIntegerField(
        'Verificado por',
        blank=True,
        null=True,
        default=None,
    )
