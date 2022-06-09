from django.views.generic.detail import DetailView

from blog.views.base import BaseView
from blog.models import Post, POST_STATUS

class PostDetailView(BaseView, DetailView):
    model = Post
