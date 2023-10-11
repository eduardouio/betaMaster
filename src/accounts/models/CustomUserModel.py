"""
    Modelos Personalizados de la Aplicación de Cuentas de Usuario.
    usamos el Correo Electrónico como nombre de usuario.
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ObjectDoesNotExist
from accounts.managers import CustomUserManager


class CustomUserModel(AbstractBaseUser):
    pass