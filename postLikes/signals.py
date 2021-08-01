from django.db.models.signals import post_save
from django.dispatch import receiver

from postApp.models import Post
from postLikes.models import Likes


@receiver(post_save, sender=Post)
def create_post_likes_list(sender, instance, created, **kwargs):
    if created:
        Likes.objects.create(post=instance)
