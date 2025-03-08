from django.contrib import admin
from django.urls import path, include
from core.views import user_login, register, index, user_logout
from tweets.views import feed
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("authentication.urls")),  # Rotas de autenticação
    path("api/", include("tweets.urls")),  # Rotas da API de tweets
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", index, name="index"),  # Página inicial
    path("register/", register, name="register"),  # Página de registro
    path("login/", user_login, name="login"),  # Página de login
    path("logout/", user_logout, name="logout"),
    path("feed/", feed, name="feed"),  # Página do feed (renderizada pelo app tweets)
]
