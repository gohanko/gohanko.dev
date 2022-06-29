from rest_framework import serializers
from blog.models.tag_or_category import TagOrCategory

class TagOrCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = TagOrCategory
        fields = [
            'pk',
            'name',
            'slug',
            'type'
        ]