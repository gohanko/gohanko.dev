from django.urls import path
from blog.views import PostDetailView, PostListView, TagListView

urlpatterns = [
   # path('/category/<slug:slug>/', PostDetailView.as_view(), name='post-category-list'),

    path('tags/', TagListView.as_view(), name='post-tags'),
    #path('/tags/<slug:slug>'),

    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/', PostListView.as_view(), name='post-list'),
]
