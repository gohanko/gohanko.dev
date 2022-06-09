from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from blog.models.post import Post, POST_STATUS

class TestLoggedInRequired(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test_user', 'test@localhost', 'test_password')

    def test_get_fail_when_not_logged_in(self):
        self.post = Post.objects.create(
            title='test_title',
            author=self.user,
            slug='test-title',
            content='test_content',
            updated_on='01/01/2022',
            created_on='01/01/2021',
            status=POST_STATUS[2][0],
        )

        response = self.client.get(reverse_lazy('post-delete', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 302)

    def test_get_pass_when_logged_in(self):
        self.post = Post.objects.create(
            title='test_title',
            author=self.user,
            slug='test-title',
            content='test_content',
            updated_on='01/01/2022',
            created_on='01/01/2021',
            status=POST_STATUS[2][0],
        )

        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse_lazy('post-delete', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
    