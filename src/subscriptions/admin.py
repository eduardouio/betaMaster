from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin


from .models import Payment, Subscription


@admin.register(Payment)
class PaymentAdmin(SimpleHistoryAdmin):
    list_display = (
        'payment_date',
        'payment_amount',
        'payment_status'
    )


@admin.register(Subscription)
class SubscriptionAdmin(SimpleHistoryAdmin):
    list_display = (
        'date_start',
        'date_end',
        'type_subscription',
        'cost'
    )
