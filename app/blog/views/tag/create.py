from django.views.generic.edit import CreateView

from blog.views.base import BaseView
from blog.models.tag import Tag

class TagCreateView(BaseView, CreateView):
    model = Tag
    template_name = 'blog/tag/tag_form.html'
    fields = ['name']