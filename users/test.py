from django.test import TestCase, Client
from django.urls import reverse
from .models import User

class UserRegistrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.signup_url = reverse('signup')
        
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        
        self.valid_data = {
            'username': 'test',
            'email': 'test@example.com',  # Adicionado email
            'password1': 'testpassword123',  # Usando password1 em vez de password
            'password2': 'testpassword123',  # Adicionado password2 para confirmação
            'first_name': 'Test',  # Opcional, mas útil
            'last_name': 'User'    # Opcional, mas útil
        }

    def test_user_registration(self):
        response = self.client.post(self.signup_url, self.valid_data)
        self.assertEqual(response.status_code, 302)  # Redirecionamento após sucesso
        self.assertTrue(User.objects.filter(username='test').exists())

    def test_user_login(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirecionamento após sucesso
        self.assertTrue('_auth_user_id' in self.client.session)

class UserModelTest(TestCase):
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
            "?name=testuser&background=random&size=128"
            "&rounded=true&bold=true&length=1"
        )
        self.assertIn(expected_url, user.avatar_url)

    def test_avatar_without_name(self):
        user = User.objects.create_user(
            username='anonymous',
            password='testpass123'
        )
        self.assertIn('name=anonymous', user.avatar_url)