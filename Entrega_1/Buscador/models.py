from django.db import models

# Create your models here.



class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Criador(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Alimento(models.Model):
    sabor = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    tamaño = models.CharField(max_length=20)
    
