from rest_framework import generics
from .serializers import ActiveTransactionViewSerializer
from payments.models import Transaction
from rest_framework.permissions import IsAuthenticated




class ActiveTransactionListView(generics.ListAPIView):
    serializer_class = ActiveTransactionViewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(item__user=self.request.user, debt__gt=0).order_by('next_due_date')
