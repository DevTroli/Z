from django.contrib import admin
from django.urls import path, include
from users.views import ZLoginView, ZSignupView, ZLogoutView, ProfileUpdateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("zweets.urls")),
    path("edit-profile/", ProfileUpdateView.as_view(), name="edit_profile"),
    path("api/", include("zweets.api.urls")),
    path("login/", ZLoginView.as_view(), name="login"),
    path("signup/", ZSignupView.as_view(), name="signup"),
    path("logout/", ZLogoutView.as_view(), name="logout"),
]
