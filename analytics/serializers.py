from rest_framework import serializers

from payments.models import Transaction


class TransactionItemSerializer(serializers.ModelSerializer):
    class Meta:
        from users.models import Item
        model = Item
        fields = '__all__'

class ActiveTransactionViewSerializer(serializers.ModelSerializer):
    from payments.serializers import TransactionStatusSerializer
    item = TransactionItemSerializer()
    status = TransactionStatusSerializer()
    class Meta:
        model = Transaction
        fields = '__all__'

