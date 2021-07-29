from django.db import models
from postApp.models import Post
from django.contrib.auth.models import User

# Create your models here.
class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usersLikes = models.ManyToManyField(User) 