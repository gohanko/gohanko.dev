from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from blog.models.tag_or_category import TagOrCategory

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

