from rest_framework import generics
from blog.models.tag_or_category import TagOrCategory
from blog.serializers.tag_or_category import TagOrCategorySerializers

class TagOrCategoryListAPIView(generics.ListCreateAPIView):
    queryset = TagOrCategory.objects.all()
    serializer_class = TagOrCategorySerializers

class TagOrCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TagOrCategory.objects.all()
    serializer_class = TagOrCategorySerializers