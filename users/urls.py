from django.urls import path
from .views import (
    UserRegisterAPIView, UserListAPIView, CustomTokenObtainPairView,
    ItemCreateAPIView, ItemListAPIView, ItemRetrieveUpdateDestroyView
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register/', UserRegisterAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),
    path('items/', ItemListAPIView.as_view()),
    path('items/create/', ItemCreateAPIView.as_view()),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view()),

    # jwt
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]