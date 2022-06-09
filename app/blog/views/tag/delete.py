from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from blog.views.base import BaseView
from blog.models.tag import Tag

class TagDeleteView(BaseView, DeleteView, PermissionRequiredMixin):
    model = Tag
    success_url = reverse_lazy('tag-list')