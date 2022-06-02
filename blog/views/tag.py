from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from blog.views.base import BaseView
from blog.models import Post, Tag

class PostListFilteredByTag(BaseView, ListView):
    model = Post
    template_name = 'blog/post/post_list.html'

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

class TagListView(BaseView, ListView):
    model = Tag
    template_name = 'blog/tag/tag_list.html'

class TagCreateView(BaseView, CreateView. PermissionRequiredMixin):
    model = Tag
    template_name = 'blog/tag/tag_form.html'
    fields = ['name']

class TagUpdateView(BaseView, UpdateView, PermissionRequiredMixin):
    model = Tag
    template_name = 'blog/tag/tag_update_form.html'
    fields = ['name']

class TagDeleteView(BaseView, DeleteView, PermissionRequiredMixin):
    model = Tag
    success_url = reverse_lazy('tag-list')