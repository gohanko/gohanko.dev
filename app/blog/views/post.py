from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from blog.models import Post, POST_STATUS
from blog.forms.post import PostCreateForm
from blog.views.base import BaseView


class PostListView(BaseView, ListView):
    model = Post
    paginate_by = 20
    template_name = 'blog/post/post_list.html'

    def get_queryset(self):
        return self.model.objects.filter(status=POST_STATUS[2][0])

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['header_title'] = 'All Posts'
        return data

class PostDetailView(BaseView, DetailView):
    model = Post
    template_name = 'blog/post/post_detail.html'

class PostCreateView(BaseView, CreateView, PermissionRequiredMixin):
    model = Post
    template_name = 'blog/post/post_form.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('post-list')

class PostUpdateView(BaseView, UpdateView, PermissionRequiredMixin):
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

class PostDeleteView(BaseView, DeleteView, PermissionRequiredMixin):
    model = Post
    success_url = reverse_lazy('post-list')