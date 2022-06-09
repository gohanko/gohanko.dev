from django.views.generic.edit import CreateView

from blog.views.base import BaseView
from blog.models.category import Category

class CategoryCreateView(BaseView, CreateView):
    model = Category
    template_name = 'blog/category/category_form.html'
    fields = ['name']