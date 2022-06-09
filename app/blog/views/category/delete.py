from django.views.generic.edit import DeleteView

from blog.views.base import BaseView
from blog.models.category import Category

class CategoryDeleteView(BaseView, DeleteView):
    model = Category
