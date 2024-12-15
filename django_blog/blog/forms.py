from django import forms
from django.contrib.auth.models import User
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm
class RegistrationForm(UserCreationForm):
    class Meta:
        model = Post
        fields = '__all__'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']
