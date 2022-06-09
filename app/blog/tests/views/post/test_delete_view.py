from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class TestPostDeleteView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test_user', 'test@localhost', 'test_password')

    def test_get_fail_when_not_logged_in(self):
        response = self.client.get(reverse_lazy('post-delete'))
        self.assertEqual(response.status_code, 302)

    def test_get_pass_when_logged_in(self):
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse_lazy('post-delete'))
        self.assertEqual(response.status_code, 200)