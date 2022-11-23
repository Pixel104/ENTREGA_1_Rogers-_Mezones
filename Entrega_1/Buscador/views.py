from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from Buscador.models import Mascota, Criador, Alimento
from Buscador.forms import CriadorFormulario, MascotaFormulario, AlimentoFormulario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import   AuthenticationForm, UserCreationForm

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


def consultas_mascota(request):

    if request.GET:
        nombre_de_mascota = request.GET.get("nombre_mascota", "")
        if nombre_de_mascota == "":
            mascotas = []
        else:
            mascotas = Mascota.objects.filter(nombre_mascota__icontains=request.GET.get("nombre_mascota"))
        return render(request, "Buscador/consultas.html", {"listado_mascotas": mascotas})

    return render(request, "Buscador/consultas.html", {"listado_mascotas": []})


def log_in(request):
   
    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("buscador-inicio")
            else:
                return render(request, "AppPixel104/login.html", {"form": formulario, "errors": "Credenciales invalidas"})

        else:
            return  render(request, "Buscador/login.html", {"form": formulario, "errors": formulario.errors})
    
    formulario = AuthenticationForm()
    return render(request, "Buscador/login.html", {"form": formulario, "errors": errors})


def Log_out(request):
    logout(request)
    return redirect("buscador-inicio")
    

