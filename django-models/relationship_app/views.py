from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from .models import Book
from .models import Library

# Create your views here.
def list_books(request):
    return render(request, 'relationship_app/list_books.html', Book.objects.all())

class LibraryListView(ListView):
    '''A class-based view inheriting from the ListView class'''
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_list_data(self, request):
        library = Library.object.get()
        format = {'library': library}
        #return format
        return render(request, 'relationship_app/list_books.html', Book.objects.all())

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})