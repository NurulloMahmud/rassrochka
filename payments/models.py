from django.db import models
from django.core.validators import RegexValidator

from users.models import Item


class TransactionStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    months = models.IntegerField(default=1)
    down_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.ForeignKey(TransactionStatus, on_delete=models.CASCADE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    next_due_date = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    installment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.item.name
    
    def save(self, *args, **kwargs):
        self.debt = self.total_amount - self.down_payment
        self.installment_amount = self.debt / self.months
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        db_table = 'transactions'
        ordering = ['-id']

class Payment(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item.name
    
    def save(self, *args, **kwargs):
        transaction_payments = self.transaction.payments.all()
        total_paid = sum(payment.amount for payment in transaction_payments)
        if total_paid + self.amount == self.transaction.total_amount:
            self.transaction.debt = 0
            self.transaction.save()
            self.next_due_date = None
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        db_table = 'payments'
        ordering = ['-id']

 