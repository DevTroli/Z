from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from zweets.models import Zweet
from .serializers import ZweetSerializer


class ZweetViewSet(viewsets.ModelViewSet):
    serializer_class = ZweetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Zweet.objects.select_related("user").prefetch_related("likes")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
