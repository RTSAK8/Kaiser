from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


# Create your views here.
def game(request: WSGIRequest):
    return render(request, 'login.html')
