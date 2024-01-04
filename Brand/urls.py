from django.urls import path
from Brand.views import game

urlpatterns = [
    path('', game, name='game'),
]
