from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required()
def homePage(request):
    return render(request, 'homepage/index.html')
