from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.views.base import BaseView
from blog.models import TagOrCategory

class TagDeleteView(LoginRequiredMixin, BaseView, DeleteView):
    model = TagOrCategory
    success_url = reverse_lazy('tag-list')