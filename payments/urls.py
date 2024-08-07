from django.urls import path
from .views import (
    TransactionListView, TransactionCreateView
)

urlpatterns = [
    path('transactions/', TransactionListView.as_view()),
    path('transactions/create/', TransactionCreateView.as_view()),
]