from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from blog.views.base import BaseView
from blog.models.tag import Tag

class TagUpdateView(BaseView, UpdateView, PermissionRequiredMixin):
    model = Tag
    template_name = 'blog/tag/tag_update_form.html'
    fields = ['name']