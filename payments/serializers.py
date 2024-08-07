from rest_framework import serializers

from .models import (
    Transaction, Payment, TransactionStatus
)


class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionStatus
        fields = '__all__'

class TransactionViewSerializer(serializers.ModelSerializer):
    from users.serializers import ItemViewSerializer
    item = ItemViewSerializer()
    status = TransactionStatusSerializer()
    
    class Meta:
        model = Transaction
        fields = '__all__'

