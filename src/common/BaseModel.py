"""
 Modelo base para todos los modelos de la aplicación, todos los modelos
    deben heredar de este modelo.

    Attributes:
        created_at (DateTime): Fecha de creación del registro.
        updated_at (DateTime): Fecha de actualización del registro.
        deleted_at (DateTime): Fecha de eliminación del registro.
        historical (HistoricalRecords): Registros históricos del modelo.

    Methods:
        save(): Guarda el registro en la base de datos.
        delete(): Elimina el registro de la base de datos.
        hard_delete(): Elimina el registro de la base de datos de forma permanente.
        restore(): Restaura un registro eliminado.
        get(): Obtiene un registro de la base de datos.
        get_or_none(): Obtiene un registro de la base de datos o None si no existe.
        get_or_404(): Obtiene un registro de la base de datos o lanza un error 404 si no existe.
        get_or_create(): Obtiene un registro de la base de datos o lo crea si no existe.
        all(): Obtiene todos los registros de la base de datos.
        filter(): Obtiene los registros de la base de datos que cumplan con los filtros.
        exclude(): Obtiene los registros de la base de datos que no cumplan con los filtros.
        order_by(): Ordena los registros de la base de datos.
        count(): Cuenta los registros de la base de datos.
        exists(): Verifica si existen registros en la base de datos.
        update(): Actualiza los registros de la base de datos que cumplan con los filtros.
        bulk_create(): Crea varios registros en la base de datos.
        bulk_update(): Actualiza varios registros en la base de datos.
        bulk_delete(): Elimina varios registros en la base de datos.
        bulk_hard_delete(): Elimina varios registros en la base de datos de forma permanente.
        bulk_restore(): Restaura varios registros eliminados en la base de datos.
        values(): Obtiene los valores de los registros de la base de datos.
        values_list(): Obtiene los valores de los registros de la base de datos.
        distinct(): Obtiene los valores de los registros de la base de datos sin repetir.
        annotate(): Anota los registros de la base de datos.
        aggregate(): Agrega los registros de la base de datos.
        first(): Obtiene el primer registro de la base de datos.
        last(): Obtiene el último registro de la base de datos.
        latest(): Obtiene el último registro de la base de datos.
        earliest(): Obtiene el primer registro de la base de datos.
        union(): Une los registros de la base de datos.
        intersection(): Intersecta los registros de la base de datos.
"""


from django.db import models
from simple_history.models import HistoricalRecords
from django.core.exceptions import ObjectDoesNotExist

# django-crum
from crum import get_current_user

# Modelo de usuario Peronalizado
from accounts.models.CustomUserModel import CustomUserModel



class BaseModel()