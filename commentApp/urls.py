from commentApp.views import deleteComment, getComments
from django.urls import path

urlpatterns = [
    path('getcomments/<int:pk>', getComments),
    path('deletecomments/<int:pk>', deleteComment),
]
