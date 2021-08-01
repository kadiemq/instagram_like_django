from commentApp.views import ListCreateComment, RetrieveUpdateDeleteComment
from django.urls import path

urlpatterns = [
    path('comments/<int:pk>', ListCreateComment.as_view()),
    path('comment/<int:pk>', RetrieveUpdateDeleteComment.as_view()),
]
