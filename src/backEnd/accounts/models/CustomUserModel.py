"""
    Modelos Personalizados de la Aplicación de Cuentas de Usuario.
    usamos el Correo Electrónico como nombre de usuario.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
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
    ('admin', 'Administrador'),
    ('guest', 'Invitado'),
    ('student', 'Estudiante'),
    ('teacher', 'Profesor'),
    ('coordinator', 'Coordinador'),
    ('school', 'Escuela'),
)

STATUS_APPROVED = (
    ('approved', 'Aprobado'),
    ('not_approved', 'No Aprobado'),
    ('pending', 'Pendiente'),
)


class CustomUserModel(AbstractUser):
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
        max_length=100
    )
    city = models.CharField(
        'Ciudad',
        max_length=100
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
    phone = models.CharField(
        'Teléfono',
        max_length=50,
        blank=True,
        null=True,
        default=None,
    )
    geolocation = models.CharField(
        'Geolocalización',
        max_length=500,
        blank=True,
        null=True,
        default=None
    )
    dni_number = models.CharField(
        'número de identificación',
        max_length=40,
        blank=True,
        help_text='Número de identificación del usuario.'
    )
    email = models.EmailField(
        'correo electrónico',
        unique=True
    )
    picture = models.ImageField(
        'imagen de perfil',
        upload_to='accounts/pictures',
        blank=True,
        help_text='Imagen de perfil del usuario.'
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
    notes = models.TextField(
        'notas',
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

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

    def __str__(self) -> str:
        return self.email
