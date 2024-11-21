from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout
from django.shortcuts import redirect

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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def custom_logout_view(request):
    logout(request)

    # Dynamically generate the logout URL
    logout_url = reverse('register')

    # Redirect to the logout URL
    return redirect(logout_url)