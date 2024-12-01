from django.shortcuts import render
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    #filter_backends = [DjangoFilterBackend]

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.get()
    serializer_class = BookSerializer
    lookup_field = ['id']
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.get()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]