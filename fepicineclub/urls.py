from django.contrib import admin
from django.urls import path, include

from fepicineclub.views import root_view, home, filmes, forum, contato

urlpatterns = [
    path('home/', home, name='home'),
    path('', root_view),
    path('filmes/', filmes, name='filmes'),
    path('forum/', forum, name='forum'),
    path('contato/', contato, name='contato'),
]  
