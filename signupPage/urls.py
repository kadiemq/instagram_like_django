from django.urls import path
from signupPage.views import SignupView

urlpatterns = [
    path('', SignupView.as_view(), name='signupPage')
]
