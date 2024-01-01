from django.urls import path
from Grand.views import menu

urlpatterns = [
    path('', menu, name='menu'),
]
