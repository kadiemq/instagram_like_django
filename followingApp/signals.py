from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from followingApp.models import Following


@receiver(post_save, sender=User)
def create_following_list(sender, instance, created, **kwargs):
    if created:
        created_object = Following.objects.create(user=instance) 
        created_object.following.add(instance)