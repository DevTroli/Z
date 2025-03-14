from django.urls import reverse
from rest_framework.test import APITestCase
from .models import User

class UserModelTests(APITestCase):
    def test_avatar_generation(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@z.com',
            password='testpass123',
            first_name='John',
            last_name='Doe'
        )
        expected_url = (
            "https://ui-avatars.com/api/"
            "?name=John+Doe&background=random&size=128"
            "&rounded=true&bold=true&length=2"
        )
        self.assertIn(expected_url, user.avatar)

    def test_avatar_without_name(self):
        user = User.objects.create_user(
            username='anonymous',
            password='testpass123'
        )
        self.assertIn('name=anonymous', user.avatar)