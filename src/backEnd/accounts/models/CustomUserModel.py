"""
    Modelos Personalizados de la Aplicación de Cuentas de Usuario.
    usamos el Correo Electrónico como nombre de usuario.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.enums import ChoicesMeta
from accounts.managers import CustomUserManager

'''
    ROLES: Lista de Roles de Usuario.
    coordinator: Puede calificar estudiantes y profesores
    guest: Invitado por defecto todos los usuarios que acceden.
    student: Estudiante calificado en la plataforma.
    teacher: Profesor calificado en la plataforma.
    school: Escuela tiene su perfil y su malla.
'''

ROLES = (
    ('ADMINISTRADOR', 'ADMINISTRADOR'),
    ('INVITADO', 'INVITADO'),
    ('ESTUDUANTE', 'ESTUDIANTE'),
    ('PROFESOR', 'PROFESOR'),
    ('COORDINADOR', 'COORDINADOR'),
    ('COLEGIO', 'ESCUELA'),
)

SEX = (
    ('MASCULINO', 'MASCULINO'),
    ('FEMENINO', 'FEMENINO'),
    ('OTRO', 'OTRO'),
)

CIVIL_STATUS = (
    ('SOLTERO', 'SOLTERO/A'),
    ('CASADO', 'CASADO/A'),
    ('DIVORCIADO', 'DIVORCIADO/A'),
    ('VIUDO', 'VIUDO/A'),
    ('SEPARADO', 'SEPARADO/A'),
    ('OTRO', 'OTRO'),
)

STATUS_APPROVED = (
    ('APROVADO', 'APROBADO'),
    ('NO_APROBADO', 'NO APROBADO'),
    ('PENDIENTE', 'PENDIENTE'),
)

LEVEL_EDUCATION = (
    ('PRIMARIA', 'PRIMARIA'),
    ('SECUNDARIA', 'SECUNDARIA'),
    ('SUPERIOR', 'SUPERIOR'),
    ('POSTGRADO', 'POSTGRADO'),
    ('MASTER', 'MASTER'),
    ('DOCTOR', 'DOCTORADO'),
    ('OTRO', 'OTRO'),
)

TYPE_DISABILITY = (
    ('VISUAL', 'VISUAL'),
    ('AUDITIVA', 'AUDITIVA'),
    ('MOTRIZ', 'MOTRIZ'),
    ('INTELECTUAL', 'INTELECTUAL'),
    ('OTRA', 'OTRA'),
)


class CustomUserModel(AbstractUser):
    username = None
    email = models.EmailField(
        'correo electrónico',
        unique=True
    )
    role = models.CharField(
        'rol usuario',
        max_length=40,
        choices=ROLES,
        default='guest',
        help_text='Rol del usuario en la plataforma.'
    )
    country = models.CharField(
        'País',
        max_length=100,
        blank=True,
        default='ECUADOR'
    )
    state = models.CharField(
        'Provincia',
        max_length=100,
        blank=True,
        null=True,
    )
    city = models.CharField(
        'Ciudad',
        max_length=100,
        blank=True,
        null=True
    )
    parroquia = models.CharField(
        'Parroquia',
        max_length=100,
        blank=True,
        null=True,
        default=None
    )
    date_of_birth = models.DateField(
        'Fecha de nacimiento',
        blank=True,
        null=True,
        default=None,
    )
    address = models.CharField(
        'Dirección',
        max_length=100,
        blank=True,
        null=True,
        default=None,
    )
    level_education = models.CharField(
        'Nivel de Educación',
        max_length=100,
        blank=True,
        null=True,
        default=None,
        choices=LEVEL_EDUCATION
    )
    profesion = models.CharField(
        'Profesión',
        max_length=100,
        blank=True,
        null=True,
    )
    phone = models.CharField(
        'Teléfono',
        max_length=50,
        blank=True,
        null=True,
        default=None,
    )
    phone_2 = models.CharField(
        'Teléfono',
        max_length=50,
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
    sex = models.CharField(
        'Sexo',
        max_length=40,
        blank=True,
        null=True,
        default=None,
        choices=SEX
    )
    dni_number = models.CharField(
        'número de identificación',
        max_length=40,
        blank=True,
        help_text='Número de identificación del usuario.'
    )
    picture = models.ImageField(
        'imagen de perfil',
        upload_to='accounts/pictures',
        blank=True,
        help_text='Imagen de perfil del usuario.'
    )
    presentation = models.TextField(
        'presentación',
        blank=True,
        null=True,
        default=None,
        help_text='Presentación del usuario'
    )
    cv = models.FileField(
        'curriculum vitae',
        upload_to='accounts/cv',
        blank=True,
        null=True,
        default=None,
    )
    is_aproved = models.CharField(
        'estado de aprobación',
        max_length=40,
        choices=STATUS_APPROVED,
        default='pending',
        help_text='Estado de aprobación del usuario.'
    )
    is_confirmed_mail = models.BooleanField(
        'correo electrónico confirmado',
        default=False,
        help_text='Estado de confirmación del correo electrónico.'
    )
    is_homescholing = models.BooleanField(
        'hace homescholing?',
        default=True,
        help_text='Habilitado para homeschooling.'
    )
    is_replacement = models.BooleanField(
        'reemplazo?',
        default=False,
        help_text='Habilitado como reemplazo'
    )
    token = models.CharField(
        'token',
        max_length=40,
        blank=True,
        help_text='Token de acceso del usuario.'
    )
    date_aproved = models.DateTimeField(
        'fecha de aprobación',
        auto_now_add=True,
        help_text='Fecha de aprobación del usuario.'
    )
    url_instagram = models.URLField(
        'url instagram',
        blank=True,
        null=True,
        default=None,
        help_text='Url de facebook del usuario.'
    )
    nationality = models.CharField(
        'nacionalidad',
        max_length=100,
        blank=True,
        null=True,
        default=None,
    )
    have_disability = models.BooleanField(
        'tiene discapacidad',
        default=False,
    )
    type_disability = models.CharField(
        'tipo de discapacidad',
        max_length=100,
        blank=True,
        null=True,
        default=None,
        choices=TYPE_DISABILITY
    )
    disability_persent = models.FloatField(
        'porcentaje discapacidad',
        default=0.0,
    )
    card_conadis = models.CharField(
        'carnet conadis',
        max_length=100,
        blank=True,
        null=True,
        default=None,
    )
    civil_status = models.CharField(
        'estado civil',
        max_length=100,
        blank=True,
        null=True,
        default=None,
        choices=CIVIL_STATUS
    )
    url_facebook = models.URLField(
        'url facebook',
        blank=True,
        null=True,
        default=None,
        help_text='Url de facebook del usuario.'
    )
    url_twiter = models.URLField(
        'url twiter',
        blank=True,
        null=True,
        default=None,
        help_text='Url de facebook del usuario.'
    )
    url_linkedin = models.URLField(
        'url linkedin',
        blank=True,
        null=True,
        default=None,
        help_text='Url de facebook del usuario.'
    )
    notes = models.TextField(
        'notas',
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
# reemplazo y homescholing LAS DOS SI
    @classmethod
    def get(cls, email):
        try:
            return cls.objects.get(email=email)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def get_user_public_data(cls, email):
        user = cls.get(email)
        if user:
            return {
                'role': user.role,
                'contact': user.contact,
                'email': user.email,
                'picture': user.picture,
                'is_aproved': user.is_aproved,
                'is_confirmed_mail': user.is_confirmed_mail,
                'date_aproved': user.date_aproved,
                'token': user.token,
                'dni_number': user.dni_number,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'notes': user.notes,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'date_joined': user.date_joined.isoformat(),
            }

    def __str__(self):
        return self.email
