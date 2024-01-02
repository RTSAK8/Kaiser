from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def menu(request: WSGIRequest):
    return render(request, 'game.html')
