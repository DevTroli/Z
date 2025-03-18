from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase
from users.models import User
from .models import Zweet


class ZweetAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testeuser", password="testpass")
        self.client.login(username="testeuser", password="testpass")

    def test_create_zweet(self):
        url = reverse("zweet-list")
        response = self.client.post(url, {"content": "Primeiro Zweet!"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Zweet.objects.count(), 1)
