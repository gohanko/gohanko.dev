from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Post

class PostDetailView(DetailView):
    model = Post

class PostListView(ListView):
    model = Post
    paginate_by = 20

