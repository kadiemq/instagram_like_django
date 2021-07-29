from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy


class loginPage(LoginView):
    template_name = 'loginPage/index.html'
    fields = '__all__'
    redirect_authenticated_user = True

