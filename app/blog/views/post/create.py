from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from blog.views.base import BaseView
from blog.models.post import Post, POST_STATUS
from blog.forms.post import PostCreateForm

class PostCreateView(LoginRequiredMixin, BaseView, CreateView):
    model = Post
    template_name = 'blog/post/post_form.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('post-list')