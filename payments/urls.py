from django.urls import path
from .views import (
    TransactionListView, TransactionCreateView, TransactionPaymentView
)

urlpatterns = [
    path('transactions/', TransactionListView.as_view()),
    path('transactions/create/', TransactionCreateView.as_view()),
    path('transactions/payment/<int:pk>/', TransactionPaymentView.as_view()),
]