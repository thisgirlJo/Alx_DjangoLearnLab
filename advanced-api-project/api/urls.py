from django.urls import path, include
from . import views
from .views import ListView, CreateView, DeleteView, DetailView, UpdateView

urlpatterns = [
    path('books', ListView.as_view),
    path('books/create', CreateView.as_view),
    path('books/update', UpdateView.as_view),
    path('books/delete', DeleteView.as_view),
    path('/books/<int:pk>/', DetailView.as_view)
]
