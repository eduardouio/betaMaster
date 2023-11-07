from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin


from .models import Payment, Subscription


@admin.register(Payment)
class PaymentAdmin(SimpleHistoryAdmin):
    list_display = (
        'subscription',
        'payment_date',
        'payment_amount',
        'payment_status',
    )

    list_filter = (
        'payment_status',
    )

    def subscription(self, obj):
        return obj.id_subscription.type_subscription


@admin.register(Subscription)
class SubscriptionAdmin(SimpleHistoryAdmin):
    list_display = (
        'date_start',
        'date_end',
        'type_subscription',
        'cost'
    )

    list_filter = (
        'type_subscription',    
    )
