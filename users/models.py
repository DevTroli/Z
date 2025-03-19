from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(blank=True, max_length=500, verbose_name="Biografia")

    @property
    def avatar_url(self):
        """Gera URL do avatar dinâmico usando UI Avatars com apenas a primeira inicial"""
        name = self.username
        name_param = name.replace(" ", "+")

        params = {
            "name": name_param,
            "background": "random",
            "size": "128",
            "rounded": "true",
            "bold": "true",
            "length": "1",
        }

        return f"https://ui-avatars.com/api/?{'&'.join([f'{k}={v}' for k,v in params.items()])}"

    def __str__(self):
        return self.username


class Follow(models.Model):
    follower = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name="followers", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "followed")
