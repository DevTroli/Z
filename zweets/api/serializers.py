from rest_framework import serializers
from zweets.models import Zweet


class ZweetSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Zweet
        fields = ["id", "user", "content", "created_at", "likes_count"]

    def get_likes_count(self, obj):
        return obj.likes.count()
