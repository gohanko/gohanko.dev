from django import forms
from django.contrib.auth.models import User

from django_summernote.widgets import SummernoteWidget

from blog.models import POST_STATUS, Post
from blog.models import TagOrCategory

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'status',
            'content',
            'categories',
            'tags'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title', 'type': 'text'}),
            'author': forms.Select(choices=User.objects.all(), attrs={'class': 'form-select'}),
            'status': forms.Select(choices=POST_STATUS, attrs={'class': 'form-select'}),
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'categories': forms.Select(choices=TagOrCategory.objects.filter(type=1), attrs={'class': 'form-select', 'multiple': ''}),
            'tags': forms.Select(choices=TagOrCategory.objects.filter(type=0), attrs={'class': 'form-select', 'multiple': ''}),
        }
