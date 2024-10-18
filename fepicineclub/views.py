from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
filmes = {
    1: {
        'titulo': 'Anjos da Noite',
        'sinopse': 'Selene é uma vampira',
        'elenco': 'Kate Beckinsale, Michael Sheen, Bill Nighy',
        'poster': '/static/cineclub/img/filme1.png',
    },
        2: {
        'titulo': 'Deadpool & Wolverine',
        'sinopse': 'Deadpool e wolverine',
        'elenco': 'Kate Beckinsale, Michael Sheen, Bill Nighy',
        'poster': '/static/cineclub/img/filme1.png',
    },
        3: {
        'titulo': 'Anjos da Noite',
        'sinopse': 'Selene é uma vampira',
        'elenco': 'Kate Beckinsale, Michael Sheen, Bill Nighy',
        'poster': '/static/cineclub/img/filme1.png',
    },
}

def home(request):
    return render(request, "home.html") #pagina home do projeto

def movie_detail(request):
    return render(request, 'movie_detail.html')