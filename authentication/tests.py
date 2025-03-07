from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticationTests(APITestCase):
    def test_register_user(self):
        url = reverse("api_register")
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass123",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_login_user(self):
        User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        url = reverse("api_login")
        data = {
            "username": "testuser",
            "password": "testpass123",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
