from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    ist_display = ('title', 'author', 'published_date')
    #list_filter = ('author', 'published_date')
    search_fields = ('title', 'content')
    #ordering = ('published_date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'post', 'created_at')
    #list_filter = ('active', 'created_at')
    search_fields = ('author', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)