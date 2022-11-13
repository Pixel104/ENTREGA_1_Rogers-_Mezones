from django.urls import path
from Buscador.views import *

urlpatterns = [
    path('', inicio, name="buscador-inicio"),
    path('mascota/', mascotas, name="buscador-mascota"),
    path('criador/', criador, name="buscador-criador"),
    path('alimento/', alimento, name="buscador-alimento"),
    path('consultas/', consultas_mascota, name="buscador-consultas"),
     
]