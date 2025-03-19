from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase
from users.models import User, Follow
from .models import Zweet, Comment


class ZweetAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testeuser", password="testpass")
        self.client.login(username="testeuser", password="testpass")

    def test_create_zweet(self):
        url = reverse("zweet-list")
        response = self.client.post(url, {"content": "Primeiro Zweet!"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Zweet.objects.count(), 1)


class FollowSystemTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password123")
        self.user2 = User.objects.create_user(username="user2", password="password123")
        self.client.login(username="user1", password="password123")

    def test_follow_user(self):
        response = self.client.post(reverse("follow", args=["user2"]))
        self.assertEqual(
            response.status_code, 302
        )  # Verifica se o redirecionamento ocorreu
        self.assertTrue(
            Follow.objects.filter(follower=self.user1, followed=self.user2).exists()
        )


class CommentTest(TestCase):
    def test_create_comment(self):
        # Cria um usuário de teste
        user = User.objects.create_user(username="testuser")
        print(f"Usuário criado: {user.username} (ID: {user.id})")

        # Cria um Zweet de teste
        zweet = Zweet.objects.create(user=user, content="Test Zweet")
        print(f"Zweet criado: ID {zweet.id}, Conteúdo: '{zweet.content}'")

        # Cria um comentário no Zweet
        comment = Comment.objects.create(user=user, zweet=zweet, content="Test Comment")
        print(f"Comentário criado: ID {comment.id}, Conteúdo: '{comment.content}'")

        # Verifica se o comentário foi associado corretamente ao Zweet
        comment_count = zweet.comments.count()
        print(f"Total de comentários no Zweet: {comment_count}")

        # Verifica se o número de comentários no Zweet é 1
        self.assertEqual(
            comment_count,
            1,
            f"O Zweet deveria ter 1 comentário, mas tem {comment_count}.",
        )
