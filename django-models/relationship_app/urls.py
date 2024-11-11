from django.urls import path
from . import views
from relationship_app.views import BookListView

#URLConf
urlpatterns = [
    path('book/', views.list_books, name='books'),
    path('library/', BookListView.as_view, name='library'),
]