from django.views.generic.detail import DetailView

from blog.views.base import BaseView
from blog.models.post import Post, POST_STATUS

class PostDetailView(BaseView, DetailView):
    model = Post
    template_name = 'blog/post/post_detail.html'