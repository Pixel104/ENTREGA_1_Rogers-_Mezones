from django.db import models

# Create your models here.



class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

class Criador(models.Model):
    nombre_criador = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()

class Alimento(models.Model):
    sabor = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    tamaño = models.CharField(max_length=20)
    
