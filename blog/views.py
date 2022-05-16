from typing import List
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Category, Tag, Post

class TagListView(ListView):
    model = Tag

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['categories'] = Category.objects.all()
        return data

class PostWithTagList(ListView):
    template_name = 'blog/post_list.html'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['categories'] = Category.objects.all()
        return data

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['categories'] = Category.objects.all()
        return data

class PostListView(ListView):
    model = Post
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['categories'] = Category.objects.all()
        return data

