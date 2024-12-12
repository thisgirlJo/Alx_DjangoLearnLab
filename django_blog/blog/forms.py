from .models import Post
from django.contrib.auth.forms import UserCreationForm
class RegistrationForm(UserCreationForm):
    class Meta:
        model = Post
        fields = '__all__'