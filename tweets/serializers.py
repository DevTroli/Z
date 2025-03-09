from rest_framework import serializers
from .models import Tweet
from authentication.serializers import UserSerializer


class TweetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    retweets_count = serializers.SerializerMethodField()
    reply_count = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = (
            "id",
            "user",
            "content",
            "created_at",
            "likes",
            "likes_count",
            "retweets_count",
            "reply_count",
            "parent_tweet",
        )
        read_only_fields = ("user", "created_at", "likes", "retweets")

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_retweets_count(self, obj):
        return obj.retweets.count()

    def get_reply_count(self, obj):
        return obj.reply_count
