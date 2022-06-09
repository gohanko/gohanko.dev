from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models.post import Post
from blog.views.base import BaseView

class PostUpdateView(LoginRequiredMixin, BaseView, UpdateView):
    model = Post
    template_name = 'blog/post/post_update_form.html'
    fields = [
        'title',
        'author',
        'content',
        'status',
        'categories',
        'tags'
    ]