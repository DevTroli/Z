from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import ZLoginView, ZSignupView, ZLogoutView, ProfileUpdateView, ProfileView, FollowView


schema_view = get_schema_view(
    openapi.Info(
        title="Z",
        default_version="v1",
        description="API Docs for Social Media Platform",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # API-DOCS
    path(
        "swagger.<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # API DRF
    path("api/", include("zweets.api.urls")),
    # Front-End
    path("admin/", admin.site.urls),
    path("", include("zweets.urls")),
    path("@<str:username>/", ProfileView.as_view(), name="profile"),
    path("@<str:username>/edit", ProfileUpdateView.as_view(), name="edit_profile"),
    path("follow/<str:username>/", FollowView.as_view(), name="follow"),
    path("login/", ZLoginView.as_view(), name="login"),
    path("signup/", ZSignupView.as_view(), name="signup"),
    path("logout/", ZLogoutView.as_view(), name="logout"),
]
