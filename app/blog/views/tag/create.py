from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from blog.views.base import BaseView
from blog.models import TagOrCategory

class TagCreateView(LoginRequiredMixin, BaseView, CreateView):
    model = TagOrCategory
    fields = ['name']