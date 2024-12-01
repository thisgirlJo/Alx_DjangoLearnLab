from django.urls import path, include
from . views
from .views import ListView, CreateView, DeleteView, DetailView, UpdateView

urlpatterns = [
    path('', ListView.as_view, name=list)
    path('', CreateView.as_view, )
]
