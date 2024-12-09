from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, UserAdmin)