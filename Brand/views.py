from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render
from Brand.models import Player
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def game(request: WSGIRequest):
    return render(request, 'login.html')


def get_info(request: WSGIRequest):
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({
            'result': 'False'
        })
    player = Player.objects.get(user=user)
    return JsonResponse({
        'result': 'success',
        'username': player.user.username,
        'photo': player.photo
    })


def signin(request: WSGIRequest):
    data = request.GET
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse({
            'result': 'username or password is incorrect'
        })
    login(request, user)
    return JsonResponse({
        'result': 'success'
    })


def register(request: WSGIRequest):
    data = request.GET
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    password_confirmation = data.get('password_confirm', '').strip()
    if not username or not password or not password_confirmation:
        return JsonResponse({
            'result': 'Username or password can not be empty'
        })
    if password != password_confirmation:
        return JsonResponse({
            'result': 'passwords do not match'
        })
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'result': 'username already exists'
        })
    user = User(username=username)
    user.set_password(password)
    user.save()
    Player.objects.create(user=user,
                          photo='/static/images/blink.png')
    login(request, user)
    return JsonResponse({
        'result': 'success'
    })


def sign_out(request: WSGIRequest):
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({
            'result': 'success'
        })
    logout(request)
    return JsonResponse({
        'result': 'success'
    })
