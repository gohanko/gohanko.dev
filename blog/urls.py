from django.urls import path
from blog.views import (
    PostWithCategoryList, 
    PostWithTagList, 
    PostDetailView, 
    PostListView, 
    TagListView
)

urlpatterns = [
    path('category/<slug:slug>/', PostWithCategoryList.as_view(), name='category-post-list'),
    path('tags/', TagListView.as_view(), name='post-tags'),
    path('tags/<slug:slug>', PostWithTagList.as_view(), name='tag-post-list'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/', PostListView.as_view(), name='post-list'),
]
