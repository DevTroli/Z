from django.contrib import admin
from django.urls import path, include
from core.views import index, register, login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("authentication.urls")),
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
]
