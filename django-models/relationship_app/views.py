from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Book, Library

# Create your views here.
def list_books(request):
    books = Book.object.all()
    format = {'list_books': books}
    return render(request, 'books/list_books.html', format)

class BookListView(ListView):
    '''A class-based view inheriting from the ListView class'''
    model = Library
    template_name = 'library/library_detail.html'

    def get_list_data(self):
        library = Library.object.get()
        format = {'library': library}
        return format