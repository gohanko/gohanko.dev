from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from blog.views.base import BaseView
from blog.models.category import Category

class CategoryDeleteView(BaseView, DeleteView, PermissionRequiredMixin):
    model = Category
