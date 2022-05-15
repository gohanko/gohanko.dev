from typing import List
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Tag, Post

class TagListView(ListView):
    model = Tag

class PostWithTagList(ListView):
    template_name = 'blog/post_list.html'

    def get_context_data(self, *args, **kwargs):
        pass

class PostDetailView(DetailView):
    model = Post

class PostListView(ListView):
    model = Post
    paginate_by = 20

