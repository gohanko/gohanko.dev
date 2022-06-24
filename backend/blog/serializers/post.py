from rest_framework import serializers
from blog.models.post import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'pk',
            'title',
            'author',
            'slug',
            'content',
            'updated_on',
            'created_on',
            'status',
            'categories',
            'tags',
        ]