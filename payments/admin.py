from django.contrib import admin
from .models import Transaction, TransactionStatus, Payment, PaymentPLan


admin.site.register(Transaction)
admin.site.register(TransactionStatus)
admin.site.register(Payment)
admin.site.register(PaymentPLan)