from rest_framework import serializers
from zweets.models import Zweet, Comment


class ZweetSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Zweet
        fields = ["id", "user", "content", "created_at", "likes_count"]

    def get_likes_count(self, obj):
        return obj.likes.count()


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "user", "content", "created_at", "replies"]

    def get_replies(self, obj):
        return CommentSerializer(obj.replies.all(), many=True).data
