from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.http.response import HttpResponse
from django.shortcuts import render
from postApp.models import Post
from .models import Likes

# Create your views here.
@receiver(post_save, sender=Post)
def createPostLikes(sender, instance, created, **kwargs):
    if created:
        Likes.objects.create(post=instance)


# @login_required()
# def getFollowingList(request):
#     user = request.user
#     followingList = user.following.all()
#     following_list = serializers.serialize('json', followingList)
#     return JsonResponse({'data': following_list})


@login_required()
def like(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    likesTable = Likes.objects.get(post=post)
    likesTable.usersLikes.add(user)
    return HttpResponse('Done')

@login_required()
def unlike(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    likesTable = Likes.objects.get(post=post)
    likesTable.usersLikes.remove(user)
    return HttpResponse('Done')