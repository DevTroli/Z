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


class FeedAuthTest(TestCase):
    def test_zweet_form_visibility(self):
        # Não autenticado - verifica texto parcial que existe no template
        response = self.client.get(reverse("zweets:feed"))
        self.assertContains(response, "Faça")
        self.assertContains(response, "login")
        self.assertContains(response, "para poder compartilhar seus Zweets")

        # Autenticado'
        user = User.objects.create_user(username="test")
        self.client.force_login(user)
        response = self.client.get(reverse("zweets:feed"))
        self.assertContains(response, '<form id="zweetForm"')
