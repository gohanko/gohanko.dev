from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

POST_STATUS = (
    (0, "Draft"),
    (1, "Hidden"),
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
    categories = models.ManyToManyField(Category, null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
