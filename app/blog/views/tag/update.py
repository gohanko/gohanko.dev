from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.views.base import BaseView
from blog.models import TagOrCategory

class TagUpdateView(LoginRequiredMixin, BaseView, UpdateView):
    model = TagOrCategory
    fields = ['name']