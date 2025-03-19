from django.contrib import admin
from django.urls import path, include
from users.views import ZLoginView, ZSignupView, ZLogoutView, ProfileUpdateView, ProfileView, FollowView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("zweets.urls")),
    path("@<str:username>/", ProfileView.as_view(), name="profile"),
    path("@<str:username>/edit", ProfileUpdateView.as_view(), name="edit_profile"),
    path("follow/<str:username>/", FollowView.as_view(), name="follow"),
    path("api/", include("zweets.api.urls")),
    path("login/", ZLoginView.as_view(), name="login"),
    path("signup/", ZSignupView.as_view(), name="signup"),
    path("logout/", ZLogoutView.as_view(), name="logout"),
]
