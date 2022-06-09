from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.views.base import BaseView
from blog.models.post import Post
from blog.forms.post import PostForm

class PostUpdateView(LoginRequiredMixin, BaseView, UpdateView):
    model = Post
    form_class = PostForm
