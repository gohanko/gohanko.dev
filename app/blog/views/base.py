from blog.models.tag import Tag
from blog.models.category import Category

class BaseView:
    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['categories'] = Category.objects.all()
        data['tags'] = Tag.objects.all()
        return data