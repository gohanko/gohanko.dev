from django.views.generic.list import ListView

from blog.views.base import BaseView
from blog.models.post import Post
from blog.models.category import Category

class PostListFilteredByCategory(BaseView, ListView):
    model = Post
    template_name = 'blog/post/post_list.html'

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