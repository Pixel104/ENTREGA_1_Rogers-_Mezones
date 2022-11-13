from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from Buscador.models import Mascota, Criador, Alimento

# Create your views here.

def  mascotas(request):
    
    return render(request, "Buscador/index.html")
