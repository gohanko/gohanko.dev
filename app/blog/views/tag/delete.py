from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from blog.views.base import BaseView
from blog.models.tag import Tag

class TagDeleteView(BaseView, DeleteView):
    model = Tag
    success_url = reverse_lazy('tag-list')