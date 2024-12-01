from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.get()
    serializer_class = BookSerializer
    lookup_field = ['id']

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.create()
    serializer_class = BookSerializer
    
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.get()
    serializer_class = BookSerializer
    
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer