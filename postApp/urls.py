from django.urls import path

from postApp.views import RetrieveUpdateDestroyPost, ListCreatePost

urlpatterns = [
    path('post/', ListCreatePost.as_view()),
    path('post/<int:pk>', RetrieveUpdateDestroyPost.as_view()),
]
