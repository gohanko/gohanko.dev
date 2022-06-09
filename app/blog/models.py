from django.db import models
from django.contrib.auth.models import User
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

POST_STATUS = (
    (0, "Draft"),
    (1, "Published but Hidden"),
    (2, "Published")
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=POST_STATUS, default=0)
    categories = models.ManyToManyField(TagOrCategory, blank=True, related_name='categories')
    tags = models.ManyToManyField(TagOrCategory, blank=True, related_name='tags')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

