from followingApp.views import follow, getFollowingList, unfollow
from django.urls import path

urlpatterns = [
    path('followinglist/', getFollowingList),
    path('follow/<int:pk>', follow),
    path('unfollow/<int:pk>', unfollow),
]