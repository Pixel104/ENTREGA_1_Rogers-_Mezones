from django.urls import path
from Buscador.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="buscador-inicio"),
    path('mascota/', mascotas, name="buscador-mascota"),
    path('criador/', criador, name="buscador-criador"),
    path('alimento/', alimento, name="buscador-alimento"),
    path('consultas/', consultas_mascota, name="buscador-consultas"),
    path('login/', log_in, name="auth-login"),
    path('logout/', Log_out, name="auth-logout")
     
]