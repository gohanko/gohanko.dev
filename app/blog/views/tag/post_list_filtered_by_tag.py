from django.views.generic.list import ListView

from blog.views.base import BaseView
from blog.models import Post
from blog.models import TagOrCategory

class PostListFilteredByTag(BaseView, ListView):
    model = Post

    def get_queryset(self):
        return self.model.objects.filter(tags__slug__in=[self.kwargs.get('slug')])

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        tag = TagOrCategory.objects.filter(slug=self.kwargs.get('slug'), type=0).first()
        if tag:
            data['header_title'] = tag.name
        else:
            data['header_title'] = '404 - Tag not found!'

        return data