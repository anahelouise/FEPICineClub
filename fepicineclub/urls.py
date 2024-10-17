from django.contrib import admin
from django.urls import path, include
from fepicineclub.views import home, root_view, my_view, user_view

urlpatterns = [
    path('home/', home),
    path('', root_view),
    path('sobre/', my_view),
    path('user/<str:username>/', user_view),
]
