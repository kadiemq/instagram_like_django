from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
from commentApp.models import Comment
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from postApp.models import Post

# Create your views here.
@login_required()
def addComment(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    comment_list = serializers.serialize('json', comments)
    return JsonResponse({'data': comment_list})

@login_required()
def getComments(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    comment_list = serializers.serialize('json', comments)
    return JsonResponse({'data': comment_list})

@login_required()
def deleteComment(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post).delete()
    return HttpResponse('Done')