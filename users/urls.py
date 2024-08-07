from django.urls import path
from .views import (
    UserRegisterAPIView, UserListAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', UserRegisterAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),

    # jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]