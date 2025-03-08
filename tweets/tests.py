# tweets/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from authentication.models import User
from .models import Tweet


class TweetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.tweet = Tweet.objects.create(user=self.user, content="Test tweet")
        self.client = APIClient()

    def test_create_tweet(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("tweet-list-create")
        data = {"content": "New tweet"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_like_tweet(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("tweet-interaction", args=[self.tweet.id, "like"])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.tweet.likes.count(), 1)
