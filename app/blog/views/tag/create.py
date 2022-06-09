from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from blog.views.base import BaseView
from blog.models.tag import Tag

class TagCreateView(BaseView, CreateView, PermissionRequiredMixin):
    model = Tag
    template_name = 'blog/tag/tag_form.html'
    fields = ['name']