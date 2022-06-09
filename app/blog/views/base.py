from blog.models import TagOrCategory

class BaseView:
    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['categories'] = TagOrCategory.objects.filter(type=1)
        data['tags'] = TagOrCategory.objects.filter(type=0)
        return data