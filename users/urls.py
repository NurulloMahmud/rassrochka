from django.urls import path
from .views import (
    UserRegisterAPIView, UserListAPIView,
    ItemCreateAPIView, ItemListAPIView, ItemRetrieveUpdateDestroyView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', UserRegisterAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),
    path('items/', ItemListAPIView.as_view()),
    path('items/create/', ItemCreateAPIView.as_view()),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view()),

    # jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]