from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from followingApp.Serializers import FollowingSerializer
from followingApp.models import Following


# @login_required()
# @api_view(('GET',))
# def following_list_view(request):
#     following_list = request.user.following.all()
#     serializer = FollowingSerializer(following_list, many=True)
#     return Response(serializer.data)

# @login_required()
# @api_view(('GET',))
# def follow_api(request, pk):
#     following_list = Following.objects.get(user=request.user)
#     user_to_follow = User.objects.get(pk=pk)
#     following_list.following.add(user_to_follow)
#     return Response('Done')

# @login_required()
# @api_view(('GET',))
# def unfollow_api(request, pk):
#     following_list = Following.objects.get(user=request.user)
#     user_to_unfollow = User.objects.get(pk=pk)
#     following_list.following.remove(user_to_unfollow)
#     return Response('Done')


class FollowingList(ListAPIView):
    """
    List all following
    """
    serializer_class = FollowingSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.request.user.following.all()


class FollowUser(UpdateAPIView):
    """
    Follow a user by their PK
    """
    serializer_class = FollowingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Following.objects.get(user=self.request.user)

    def patch(self, request, pk, *args, **kwargs):
        user_to_follow = User.objects.get(pk=pk)
        self.get_queryset().following.add(user_to_follow)
        return Response('Done')


class UnfollowUser(UpdateAPIView):
    """
    Unfollow a user by their PK
    """
    serializer_class = FollowingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Following.objects.get(user=self.request.user)

    def patch(self, request, pk, *args, **kwargs):
        user_to_follow = User.objects.get(pk=pk)
        self.get_queryset().following.remove(user_to_follow)
        return Response('Done')
