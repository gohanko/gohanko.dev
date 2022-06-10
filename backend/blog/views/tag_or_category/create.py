from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from blog.views.base import BaseView
from blog.models.tag_or_category import TagOrCategory

class TagOrCategoryCreateView(LoginRequiredMixin, BaseView, CreateView):
    model = TagOrCategory
    fields = ['name']