from django.db import models

# Create your models here.



class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"Nombre: {self.nombre_mascota} || Raza: {self.raza} || Color: {self.color} || Fecha Nacimiento: {self.fecha_nacimiento}"


class Criador(models.Model):
    nombre_criador = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"Nombre: {self.nombre_criador} || Apellido: {self.apellido} || Provincia: {self.provincia} || Fecha Nac.: {self.fecha_nacimiento}"


class Alimento(models.Model):
    sabor = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    tamaño = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Sabor: {self.sabor} || Raza: {self.raza} || Tamaño: {self.tamaño}"
