from django.shortcuts import render


# Create your views here.
def signupPage(request):
    return render(request, 'signupPage/index.html')
