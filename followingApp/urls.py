from followingApp.views import FollowingList, FollowUser, UnfollowUser
from django.urls import path


urlpatterns = [
    path('followinglist/', FollowingList.as_view()),
    path('follow/<int:pk>/', FollowUser.as_view()),
    path('unfollow/<int:pk>/', UnfollowUser.as_view()),
]
