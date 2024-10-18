from django.contrib import admin
from django.urls import path, include

from fepicineclub.views import home, movie_detail

urlpatterns = [
    path('', home),
    path('movie_detail/<int:movie_id>/', movie_detail, name='movie_detail'),
]  
