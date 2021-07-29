from django.urls import path

from loginPage.views import loginPage

urlpatterns = [
    path('', loginPage.as_view(), name='loginPage')
]
