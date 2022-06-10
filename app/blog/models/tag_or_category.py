from django.db import models
from django.template.defaultfilters import slugify

TAG_OR_CATEGORY_TYPE = (
    (0, 'Tag'),
    (1, 'Category')
)

class TagOrCategory(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.IntegerField(choices=TAG_OR_CATEGORY_TYPE, default=0)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TagOrCategory, self).save(*args, **kwargs)
