from django.urls import path
from .views import (
    ActiveTransactionListView
)



urlpatterns = [
    path('transactions/active/', ActiveTransactionListView.as_view()),
]