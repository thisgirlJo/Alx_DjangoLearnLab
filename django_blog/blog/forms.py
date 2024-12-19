from django import forms
from django.contrib.auth.models import User
from .models import Post, Profile, Comment
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
    
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']

class CommentForm(forms.ModelForm): # This is to facilitate comment creation and updating
    model = Comment
    fields = ['author', 'content']

