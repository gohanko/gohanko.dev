from django.contrib import admin
from blog.models import Tag, Category, Post

class TagAndCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAndCategoryAdmin)
admin.site.register(Category, TagAndCategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'updated_on')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)