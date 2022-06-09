from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from blog.views.base import BaseView
from blog.models.category import Category

class CategoryCreateView(BaseView, CreateView, PermissionRequiredMixin):
    model = Category
    template_name = 'blog/category/category_form.html'
    fields = ['name']