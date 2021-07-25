from django.urls import path
from signupPage.views import signupPage

urlpatterns = [
    path('', signupPage, name='signupPage')
]
