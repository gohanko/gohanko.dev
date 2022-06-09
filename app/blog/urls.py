from django.urls import path

from blog.views.category import (
    PostListFilteredByCategory,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)
from blog.views.tag import (
    PostListFilteredByTag,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)
from blog.views.post import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/update/<slug:slug>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category/delete/<slug:slug>/', CategoryDeleteView.as_view(), name='category-delete'),
    path('category/<slug:slug>/', PostListFilteredByCategory.as_view(), name='post-list-filtered-by-category'),
    
    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
    path('tags/update/<slug:slug>/', TagUpdateView.as_view(), name='tag-update'),
    path('tags/delete/<slug:slug>/', TagDeleteView.as_view(), name='tag-delete'),
    path('tags/<slug:slug>/', PostListFilteredByTag.as_view(), name='post-list-filtered-by-tag'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/delete/<slug:slug>/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/update/<slug:slug>/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/', PostListView.as_view(), name='post-list'),
]
