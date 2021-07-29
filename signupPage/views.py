from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from signupPage.Forms import CreateUserForm


class SignupView(CreateView):
    template_name = 'signupPage/index.html'
    success_url = 'login'
    form_class = CreateUserForm
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.method == 'POST':
            return redirect('homePage')

        return super(SignupView, self).dispatch(request, *args, **kwargs)
