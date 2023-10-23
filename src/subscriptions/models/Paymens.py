from django.db import models
from accounts.models import CustomUserModel
from subscriptions.models import SubscriptionModel
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
    id_user = models.ForeignKey(
        CustomUserModel
    )
    id_subscription = models.ForeignKey(
        SubscriptionModel
    )
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    payment_status = models.CharField(
        max_length=30,
        choices=PAYMENT_STATUS,
        default='PENDING'
    )
    transaction_id = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    bank_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    owner_account = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    dni_owner_account = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    account_number = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
