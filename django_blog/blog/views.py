from django.shortcuts import render, redirect
#from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Account created for {username}!') # Show sucess message when account is created
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    # This view can only be accessed by authenticated users
    return render(request, 'blog/base.html')
