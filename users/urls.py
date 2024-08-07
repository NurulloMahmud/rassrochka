from django.urls import path
from .views import UserRegisterAPIView


urlpatterns = ['register/', UserRegisterAPIView.as_view()]