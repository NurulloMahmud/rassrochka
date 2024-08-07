from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from datetime import datetime

from .serializers import (
    TransactionViewSerializer
)
from .models import (
    Transaction, TransactionStatus, Payment
)

from .utils import (
    get_next_month_same_day, get_next_week_same_day,
    is_valid_email, is_valid_phone_number, get_next_day
)
    
class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionViewSerializer
    queryset = Transaction.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(item__user=self.request.user)

class TransactionCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        from users.models import Item
        # get payment plan fields
        months = request.data.get('months', 0)

        if not months:
            return Response({'error': 'Please provide all required fields.'}, status=400)

        item_id = request.data.get('item_id')
        status_obj = TransactionStatus.objects.get_or_create(name="In Process")[0]
        item_obj = Item.objects.filter(id=item_id, user=self.request.user).first()

        if not item_obj:
            return Response({'error': 'Item not found.'}, status=404)
        
        customer_name = request.data.get('customer_name')
        customer_phone_number = request.data.get('customer_phone_number')
        total_amount = request.data.get('total_amount')
        down_payment = request.data.get('down_payment', 0)

        if not customer_name or not customer_phone_number or not total_amount:
            return Response({'error': 'Please provide all required fields.'}, status=400)

        if not is_valid_phone_number(customer_phone_number):
            return Response({'error': 'Invalid phone number.'}, status=400)
        
        debt = total_amount - down_payment
        if debt < 0:
            return Response({'error': 'Down payment cannot be greater than total amount.'}, status=400)
        
        today = datetime.today()
        today_str = today.strftime('%Y-%m-%d')
        next_due_date = get_next_month_same_day(today_str, 1)

        if down_payment == total_amount:
            next_due_date = None
            debt = 0
            status_obj = TransactionStatus.objects.get_or_create(name="Paid")[0]

        Transaction.objects.create(
            item=item_obj,
            customer_name=customer_name,
            customer_phone_number=customer_phone_number,
            total_amount=total_amount,
            months=int(months),
            down_payment=down_payment,
            status=status_obj,
            debt=debt,
            next_due_date=next_due_date
        )

        return Response({'message': 'Transaction created successfully.'}, status=201)

class TransactionPaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        transaction_obj = Transaction.objects.filter(pk=pk, item__user=self.request.user).first()
        if not transaction_obj:
            return Response({'error': 'Transaction not found.'}, status=404)
        
        payment_obj = Payment.objects.create(
            transaction=transaction_obj,
            amount=transaction_obj.installment_amount
        )

        last_payment_date = transaction_obj.next_due_date
        last_payment_date_str = last_payment_date.strftime('%Y-%m-%d')
        next_due_date = get_next_month_same_day(last_payment_date_str, 1)

        if transaction_obj.debt == 0:
            transaction_obj.status = TransactionStatus.objects.get_or_create(name="Paid")[0]
            next_due_date = None
            transaction_obj.debt = 0

        transaction_obj.debt -= transaction_obj.installment_amount
        transaction_obj.next_due_date = next_due_date
        transaction_obj.save()

        return Response({'message': 'Payment created successfully.'}, status=201)

class TransactionDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        transaction_obj = Transaction.objects.filter(pk=pk, item__user=self.request.user).first()
        if not transaction_obj:
            return Response({'error': 'Transaction not found.'}, status=404)
        
        transaction_obj.delete()
        return Response({'message': 'Transaction deleted successfully.'}, status=200)

