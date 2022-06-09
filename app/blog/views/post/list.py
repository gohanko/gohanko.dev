from django.views.generic.list import ListView

from blog.views.base import BaseView
from blog.models.post import Post, POST_STATUS

class PostListView(BaseView, ListView):
    model = Post
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.filter(status=POST_STATUS[2][0])

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['header_title'] = 'All Posts'
        return data
