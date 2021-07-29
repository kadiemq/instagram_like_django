from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from followingApp.models import Following
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers
 
# Create your views here.
@receiver(post_save, sender=User)
def createFollowing(sender, instance, created, **kwargs):
    if created:
        Following.objects.create(user=instance) 

@login_required()
def getFollowingList(request):
    user = request.user
    followingList = user.following.all()
    following_list = serializers.serialize('json', followingList)
    return JsonResponse({'data': following_list})


@login_required()
def follow(request, pk):
    user = request.user
    userFollowingTable = Following.objects.get(user=user)
    userToFollow = User.objects.get(pk=pk)
    userFollowingTable.following.add(userToFollow)
    return HttpResponse('Done')

@login_required()
def unfollow(request, pk):
    user = request.user
    userFollowingTable = Following.objects.get(user=user)
    userToFollow = User.objects.get(pk=pk)
    userFollowingTable.following.remove(userToFollow)
    return HttpResponse('Done')

