from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from Buscador.models import Mascota, Criador, Alimento
from Buscador.forms import CriadorFormulario, MascotaFormulario, AlimentoFormulario

# Create your views here.

def  inicio(request):
    
    return render(request, "Buscador/index.html")

def  mascotas(request):

    if request.method == "POST":
        formulario = MascotaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            mascota = Mascota(nombre_mascota=data["nombre_mascota"], raza=data["raza"], color=data["color"], fecha_nacimiento=data["fecha_nacimiento"] )
            mascota.save()
    
    formulario = MascotaFormulario()

    return render(request, "Buscador/mascota.html", {"formulario": formulario})



def  criador(request):

    if request.method == "POST":
        formulario = CriadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            criador = Criador(nombre_criador=data["nombre_criador"], apellido=data["apellido"], provincia=data["provincia"], fecha_nacimiento=data["fecha_nacimiento"] )
            criador.save()
    
    formulario = CriadorFormulario()
    
    return render(request, "Buscador/criador.html", {"formulario": formulario})




def  alimento(request):

    if request.method == "POST":
        formulario = AlimentoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            alimento = Alimento(sabor=data["sabor"], raza=data["raza"], tamaño=data["tamaño"])
            alimento.save()

    formulario = AlimentoFormulario()

    return render(request, "Buscador/alimento.html", {"formulario": formulario})