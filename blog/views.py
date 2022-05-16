from typing import List
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import POST_STATUS, Category, Tag, Post

class BaseView:
    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['categories'] = Category.objects.all()
        data['tags'] = Tag.objects.all()
        return data

class TagListView(BaseView, ListView):
    model = Tag

class PostWithCategoryList(BaseView, ListView):
    model = Post

    def get_queryset(self):
        return self.model.objects.filter(categories__slug__in=[self.kwargs.get('slug')])

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        category = Category.objects.filter(slug=self.kwargs.get('slug')).first()
        if category:
            data['header_title'] = category.name
        else:
            data['header_title'] = '404 - Category not found!'

        return data

class PostWithTagList(BaseView, ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return self.model.objects.filter(tags__slug__in=[self.kwargs.get('slug')])

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        tag = Tag.objects.filter(slug=self.kwargs.get('slug')).first()
        if tag:
            data['header_title'] = tag.name
        else:
            data['header_title'] = '404 - Tag not found!'

        return data

class PostDetailView(BaseView, DetailView):
    model = Post

class PostListView(BaseView, ListView):
    model = Post
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.filter(status=POST_STATUS[2][0])

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['header_title'] = 'All Posts'
        return data