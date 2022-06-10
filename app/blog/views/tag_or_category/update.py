from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.views.base import BaseView
from blog.models.tag_or_category import TagOrCategory

class TagOrCategoryUpdateView(LoginRequiredMixin, BaseView, UpdateView):
    model = TagOrCategory
    fields = ['name']