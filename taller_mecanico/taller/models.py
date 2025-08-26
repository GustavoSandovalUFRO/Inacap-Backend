# taller/models.py
from django.db import models

class Mecanico(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    dueño = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.modelo} [{self.patente}]"

class Procedimiento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE, related_name='procedimientos')
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='procedimientos')

    def __str__(self):
        return f"{self.nombre} - {self.vehiculo.patente}"