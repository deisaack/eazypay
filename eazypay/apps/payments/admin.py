from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('mobile_number', 'till_number', 'transaction_ref_no', 'amount', )

admin.site.register(Payment, PaymentAdmin)
