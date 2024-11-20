from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
def list_books(request):
    return render(request, 'relationship_app/list_books.html', Book.objects.all())

class LibraryListView(ListView, DetailView):
    '''A class-based view inheriting from the ListView class'''
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_list_data(self):
        library = Library.object.get()
        format = {'library': library}
        #return format
        return render(request, 'relationship_app/list_books.html', Book.objects.all())

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'