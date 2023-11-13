from django.db import models
from common.models import BaseModel
from .CustomUserModel import CustomUserModel

TYPE_REFERENCES = (
    ('personal', 'PERSONAL'),
    ('professional', 'PROFESIONAL'),
)

TYPE_RELATIONSHIP = (
    ('family', 'FAMILIAR'),
    ('boss', 'JEFE INMEDIATO'),
    ('buddy', 'COMPAÑERO DE TRABAJO'),
    ('other', 'OTRO'),
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
    enterprise = models.CharField(
        'Empresa',
        max_length=100
    )
    name_contact = models.CharField(
        'Nombre de Contacto',
        max_length=100
    )
    phone_contact = models.CharField(
        'Teléfono de Contacto',
        max_length=40
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
        default=None,
    )
    verification_by = models.PositiveIntegerField(
        'Verificado por',
        default=None,
    )
