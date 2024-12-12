"""Models"""
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model # Current User Model

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self) -> str:
        return f"{self.name}"


class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"

ROLES = (
    ("Admin", "Admin"),
    ("Librarian", "Librarian"),
    ("Member", "Member"),
)

#User = get_user_model

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLES)

    def __str__(self) -> str:
        return f"{self.user}'s Profile"