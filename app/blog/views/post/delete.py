from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

from blog.views.base import BaseView
from blog.models.post import Post

class PostDeleteView(LoginRequiredMixin, BaseView, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')