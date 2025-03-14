# users/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .api import (
    UserRegisterView,
    CustomTokenObtainPairView,
    UserProfileView
)

urlpatterns = [
    # Autenticação
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Perfil do Usuário
    path('users/me/', UserProfileView.as_view(), name='user-profile'),
]