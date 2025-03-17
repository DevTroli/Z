from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ZweetViewSet

router = DefaultRouter()
router.register(r"zweets", ZweetViewSet, basename="zweet")

urlpatterns = [
    path("", include(router.urls)),
]
