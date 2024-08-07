from django.contrib import admin
from .models import Transaction, TransactionStatus, Payment


admin.site.register(Transaction)
admin.site.register(TransactionStatus)
admin.site.register(Payment)