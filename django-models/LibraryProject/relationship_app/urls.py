from django.urls import path
from . import views
from .views import BookListView
from .views import list_books

#URLConf
urlpatterns = [
    path('book/', views.list_books, name='books'),
    path('library/', LibraryDetailView.as_view, name='library'),
]