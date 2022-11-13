from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from Buscador.models import Mascota, Criador, Alimento

# Create your views here.

def  inicio(request):
    
    return render(request, "Buscador/index.html")

def  mascotas(request):
    
    return render(request, "Buscador/mascota.html")

def  criador(request):
    
    return render(request, "Buscador/criador.html")

def  alimento(request):
    
    return render(request, "Buscador/alimento.html")