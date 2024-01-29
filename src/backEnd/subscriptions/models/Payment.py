from django.db import models
from subscriptions.models import Subscription
from accounts.models import BankAccount
from common import BaseModel

PAYMENT_STATUS = (
    ('PENIDENTE', 'PENDIENTE'),
    ('PAGADO', 'PAGADO'),
    ('ERROR', 'ERROR'),
    ('DEVUELTO', 'DEVUELTO'),
    ('CANCELADO', 'CANCELADO'),
)


class Payment(BaseModel):
    id_payment = models.AutoField(primary_key=True)
    id_subscription = models.ForeignKey(
        Subscription,
        on_delete=models.RESTRICT
    )
    id_bank = models.ForeignKey(
        BankAccount,
        on_delete=models.RESTRICT
    )
    payment_date = models.DateTimeField(
        'Fecha de Pago',
        auto_now_add=True
    )
    payment_amount = models.FloatField(
        'Monto de Pago',
        default=0.0
    )
    payment_status = models.CharField(
        'Estado de Pago',
        max_length=30,
        choices=PAYMENT_STATUS,
        default='PENDIENTE'
    )
    transaction_id = models.CharField(
        'Identificador de Transacción',
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
    photo_voucher = models.ImageField(
        'Foto de Voucher',
        upload_to='payment/vouchers/',
        blank=True,
        null=True,
        default=None
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
