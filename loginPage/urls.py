from django.urls import path

from loginPage.views import loginPage

urlpatterns = [
    path('', loginPage, name='loginPage')
]
