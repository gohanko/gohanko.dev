from blog.models import Category, Tag

class BaseView:
    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['categories'] = Category.objects.all()
        data['tags'] = Tag.objects.all()
        return data