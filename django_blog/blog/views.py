from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,UserUpdateForm, ProfileUpdateForm, PostCreateForm
from .models import Post
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Account created for {username}!') # Show sucess message when account is created
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('home')  # Ensure redirect happens after saving
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'blog/dashboard.html', context)

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'  # Custom template for login
    redirect_authenticated_user = True       # Redirect already authenticated users
    success_url = reverse_lazy('home')       # Default redirect after successful login

    def get_success_url(self):
        # Optionally customize the success URL dynamically
        return self.success_url or super().get_success_url()

    def form_valid(self, form):
        # Additional logic after successful form validation
        messages.success(self.request, "Welcome back!")
        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle invalid form submission
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)


def base_view(request):
    return render(request, 'blog/dashboard.html')

def home_view(request):
    return render(request, 'blog/home.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'
    fields = '__all__'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_detail'
    #queryset = Post.objects.all()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post   
    template_name = 'blog/post_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    def form_valid(self, form):
        # Ensure the author remains the same
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # Check if the current user is the author of the post
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = '/'

    def test_func(self):
        # Check if the current user is the author of the post
        post = self.get_object()
        return self.request.user == post.author