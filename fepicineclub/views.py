from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html") #pagina home do projeto

def root_view(request):
    return render(request, "home.html") #pagina inicial do runserver

def filmes(request):
    return render(request, "catalogofilmes.html") #Pagina sobre a desenvolvedora

def forum(request):
    return render(request, "tropas.html") #Pagina sobre as tropas

def contato(request):
    return render(request, "contato.html")