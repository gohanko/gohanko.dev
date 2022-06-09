from django.views.generic.edit import UpdateView

from blog.views.base import BaseView
from blog.models.category import Category

class CategoryUpdateView(BaseView, UpdateView):
    model = Category
    template_name = 'blog/category/category_update_form.html'
    fields = ['name']