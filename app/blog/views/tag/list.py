from django.views.generic.list import ListView

from blog.views.base import BaseView
from blog.models.tag import Tag

class TagListView(BaseView, ListView):
    model = Tag
    template_name = 'blog/tag/tag_list.html'