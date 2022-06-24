from django.urls import path

from blog.views.tag_or_category import PostListFilteredByTagOrCategory, TagOrCategoryCreateView, TagOrCategoryUpdateView, TagOrCategoryDeleteView
from blog.views.post import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from blog.views.post.api import PostListAPIView, PostDetailAPIView
from blog.views.tag_or_category.api import TagOrCategoryListAPIView, TagOrCategoryDetailAPIView

urlpatterns = [
    path('api/v1/tags_or_category/', TagOrCategoryListAPIView.as_view(), name='api-tag-or-category-list'),
    path('api/v1/tags_or_category/<int:pk>/', TagOrCategoryDetailAPIView.as_view(), name='api-tag-or-category-crud'),

    path('tags_or_category/create/', TagOrCategoryCreateView.as_view(), name='tag-create'),
    path('tags_or_category/update/<slug:slug>/', TagOrCategoryUpdateView.as_view(), name='tag-update'),
    path('tags_or_category/delete/<slug:slug>/', TagOrCategoryDeleteView.as_view(), name='tag-delete'),
    path('tags_or_category/<slug:slug>/', PostListFilteredByTagOrCategory.as_view(), name='post-list-filtered-by-tag'),
    
    path('api/v1/posts/', PostListAPIView.as_view(), name='user-list'),
    path('api/v1/posts/<int:pk>/', PostDetailAPIView.as_view(), name='api-post-crud'),
    
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/delete/<slug:slug>/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/update/<slug:slug>/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/', PostListView.as_view(), name='post-list'),
]
