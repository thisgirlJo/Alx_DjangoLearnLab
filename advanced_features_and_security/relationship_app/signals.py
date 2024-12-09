from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import UserProfile

user = get_user_model()

@receiver(post_save, sender=user)

def create_user_profile(sender, instance, created, **kwargs):
    print("Sender --> ", sender)
    print("instance --> ", instance)
    print("created --> ", created)
    if created:
        UserProfile.objects.create(user=instance)
