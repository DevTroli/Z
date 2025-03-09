from django.db import models
from authentication.models import User


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="liked_tweets", blank=True)
    retweets = models.ManyToManyField(User, related_name="retweeted_tweets", blank=True)
    parent_tweet = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )

    def __str__(self):
        return f"Tweet by {self.user.username}"

    @property
    def reply_count(self):
        return self.replies.count()
