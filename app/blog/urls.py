from django.urls import path

from blog.views.tag import (
    PostListFilteredByTag,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)
from blog.views.post import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
    path('tags/update/<slug:slug>/', TagUpdateView.as_view(), name='tag-update'),
    path('tags/delete/<slug:slug>/', TagDeleteView.as_view(), name='tag-delete'),
    path('tags/<slug:slug>/', PostListFilteredByTag.as_view(), name='post-list-filtered-by-tag'),
    
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/delete/<slug:slug>/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/update/<slug:slug>/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/', PostListView.as_view(), name='post-list'),
]
