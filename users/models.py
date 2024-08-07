from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(validators=[phone_regex], unique=True, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'
        ordering = ['-id']

class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
        db_table = 'statuses'
        ordering = ['id']

class Item(models.Model):
    name = models.CharField(max_length=100)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        db_table = 'items'
        ordering = ['-id']
