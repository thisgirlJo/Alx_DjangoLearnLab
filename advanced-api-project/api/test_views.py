from rest_framework.test import APIRequestFactory
from django.test import TestCase
from .views import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Book
class TestCaseCrud(TestCase):
    def setUp(self):
        Book.objects.create(title="1984", publication_year=2021, author='Judith ogbole')
        Book.objects.create(title='Hogwarts', publication_year=1950, author='Lily Allen')
        
    def test_create_book(self):
        1984 = Book.objects.get(title="1984")
        Hogwarts = Book.objects.get(title="Hogwarts")
        self.assertEqual                 