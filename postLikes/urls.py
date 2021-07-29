from postLikes.views import like, unlike
from django.urls import path

urlpatterns = [
    path('like/<int:pk>', like),
    path('unlike/<int:pk>', unlike),
]