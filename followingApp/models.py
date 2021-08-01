from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ManyToManyField(User, related_name='usersFollowing')

    class Meta:
        unique_together = [['user']]

    # def __str__(self):
    #     return f'{user} followings'
