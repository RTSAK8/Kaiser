from django.urls import path
from Brand.views import game, get_info, signin, register, sign_out

urlpatterns = [
    path('', game, name='game'),
    path('get_info', get_info, name='get_info'),
    path('signin', signin, name='signin'),
    path('register', register, name='register'),
    path('logout', sign_out, name='logout')
]
