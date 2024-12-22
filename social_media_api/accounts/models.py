from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class User_Custom(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField()
    followers = models.ManyToManyField('self', symmetrical=False)


    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Unique related_name to avoid conflicts
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Unique related_name
        blank=True,
    )
    def __str__(self):
        return self.username