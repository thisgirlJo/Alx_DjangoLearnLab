from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,UserUpdateForm, ProfileUpdateForm, PostCreateForm
from .models import Post

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Account created for {username}!') # Show sucess message when account is created
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile_view(request):
    # This view can only be accessed by authenticated users
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            return redirect('profile')
        else:
            user_form = UserUpdateForm(instance=request.user)
            profile_form = ProfileUpdateForm(instance=request.user.profile)
            
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
    return render(request, 'blog/dashboard.html', context)

def base_view(request):
    return render(request, 'blog/base.html')

def home_view(request):
    return render(request, 'blog/home.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'
    fields = '__all__'


class PostDetailView():
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_detail'
    #queryset = Post.objects.all()


class PostCreateView(CreateView):
    model = Post   
    template_name = 'blog/post_create.html'

class PostUpdateView():
    model = Post
    template_name = 'blog/post_update.html'

class PostDeleteView():
    model = Post
    template_name = 'blog/post_delete.html'