from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path("register/", views.register_user, name="api_register"),
    path("login/", TokenObtainPairView.as_view(), name="api_login"),
]
