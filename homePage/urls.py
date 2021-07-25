from django.urls import path

from homePage.views import homePage

urlpatterns = [
    path('', homePage, name='homePage')
]
