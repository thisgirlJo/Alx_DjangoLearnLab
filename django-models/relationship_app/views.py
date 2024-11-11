from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Book
from .models import Library

# Create your views here.
def list_books(request):
    return render(request, 'relationship_app/list_books.html', Book.objects.all())

class BookListView(ListView):
    '''A class-based view inheriting from the ListView class'''
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_list_data(self):
        library = Library.object.get()
        format = {'library': library}
        return format
        #return render(request, 'relationship_app/list_books.html', Book.objects.all())