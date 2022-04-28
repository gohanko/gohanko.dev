from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

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
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
