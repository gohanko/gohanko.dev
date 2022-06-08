from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blog.models.post import Post
from blog.models.tag import Tag
from blog.models.category import Category

class TagAndCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAndCategoryAdmin)
admin.site.register(Category, TagAndCategoryAdmin)

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'updated_on')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)