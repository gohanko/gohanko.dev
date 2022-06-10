from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blog.models.post import Post
from blog.models.tag_or_category import TagOrCategory

class TagOrCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(TagOrCategory, TagOrCategoryAdmin)

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'updated_on')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)