from django.urls import path
from blog.views import PostDetailView, PostListView

urlpatterns = [
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('', PostListView.as_view(), name='post-list'),
]
