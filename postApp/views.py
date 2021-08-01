from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from followingApp.models import Following
from postApp.models import Post
from postApp.serializer import PostSerializer


class ListCreatePost(ListCreateAPIView):
    """
    Create a post or list all posts (From following)
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        following = Following.objects.get(user=self.request.user).following.all()

        return following

    def list(self, request, *args, **kwargs):
        data = []

        queryset = self.get_queryset()
        for user in queryset:
            posts = user.post_set
            serializer = PostSerializer(posts, many=True)
            data.append(serializer.data)

        data = sum(data, [])

        return Response(data)


class RetrieveUpdateDestroyPost(RetrieveUpdateDestroyAPIView):
    """
    Get, update, and delete a single post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
