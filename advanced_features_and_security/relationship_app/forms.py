from django.contrib.auth.forms import UserCreationForm
from . import models
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")