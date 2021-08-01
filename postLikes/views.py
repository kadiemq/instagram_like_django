from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from postApp.models import Post
from .models import Likes
from .serializer import PostLikesSerializer


class LikesList(RetrieveAPIView):
    serializer_class = PostLikesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        post = Likes.objects.get(post=pk).usersLikes.all()
        return post

    def retrieve(self, request, *args, **kwargs):
        data = []

        queryset = self.get_queryset()
        # for user in queryset:

        posts = queryset[0].likes_set
        serializer = PostLikesSerializer(posts, many=True)
        data.append(serializer.data)

        data = sum(data, [])

        return Response(data)


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
