from postLikes.views import like, unlike, LikesList
from django.urls import path

urlpatterns = [
    path('like/<int:pk>', like),
    path('unlike/<int:pk>', unlike),

    path('likes/<int:pk>', LikesList.as_view()),
]
