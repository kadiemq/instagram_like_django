from django.db import models
from postApp.models import Post
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
