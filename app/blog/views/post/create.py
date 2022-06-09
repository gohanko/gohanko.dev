from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from blog.views.base import BaseView
from blog.models.post import Post
from blog.forms.post import PostForm

class PostCreateView(LoginRequiredMixin, BaseView, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post-list')
