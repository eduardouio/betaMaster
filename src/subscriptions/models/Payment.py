from django.db import models
from subscriptions.models import Subscription
from common import BaseModel

PAYMENT_STATUS = (
    ('PENDING', 'PENDING'),
    ('PAID', 'PAID'),
    ('FAILED', 'FAILED'),
    ('REFUNDED', 'REFUNDED'),
    ('CANCELLED', 'CANCELLED'),
    ('EXPIRED', 'EXPIRED'),
)


class Payment(BaseModel):
    id_payment = models.AutoField(primary_key=True)
    id_subscription = models.ForeignKey(
        Subscription,
        on_delete=models.RESTRICT
    )
    payment_date = models.DateTimeField(
        'Fecha de Pago',
        auto_now_add=True
    )
    payment_amount = models.DecimalField(
        'Monto de Pago',
        max_digits=10,
        decimal_places=2
    )
    payment_status = models.CharField(
        'Estado de Pago',
        max_length=30,
        choices=PAYMENT_STATUS,
        default='PENDING'
    )
    transaction_id = models.CharField(
        'Identificador de Transacción',
        max_length=100,
        null=True,
        blank=True
    )
    bank_name = models.CharField(
        'Nombre de Banco',
        max_length=100,
        null=True,
        blank=True
    )
    owner_account = models.CharField(
        'Cuenta de Origen Pago',
        max_length=100,
        null=True,
        blank=True
    )
    dni_owner_account = models.CharField(
        'DNI de Titular de Cuenta',
        max_length=100,
        null=True,
        blank=True
    )
    account_number = models.CharField(
        'Número de Cuenta',
        max_length=100,
        null=True,
        blank=True
    )
    account_destination = models.CharField(
        'Cuenta de Destino',
        max_length=100,
        null=True,
        blank=True
    )
    bank_destination = models.CharField(
        'Banco de Destino',
        max_length=100,
        null=True,
        blank=True
    )
    invoice_number = models.CharField(
        'Número de Factura',
        max_length=100,
        null=True,
        blank=True
    )
    invoice_xml = models.TextField(
        'XML de Factura',
        blank=True,
        null=True,
        default=None
    )
