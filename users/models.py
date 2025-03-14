from django.contrib.auth.models import AbstractUser
from django.core.cache import cache
from django.db import models
from urllib.parse import quote

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True, null=True)  # Tornado opcional
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)

    @property
    def avatar(self):
        """Gera URL do avatar dinâmico usando UI Avatars"""
        name = self.get_full_name() or self.username
        name_param = name.replace(' ', '+')
        params = {
            'name': name_param,
            'background': 'random',
            'size': '128',
            'rounded': 'true',
            'bold': 'true',
            'length': '1' if len(name.split()) == 0 else '2'
        }
        return f"https://ui-avatars.com/api/?{'&'.join([f'{k}={v}' for k,v in params.items()])}"
