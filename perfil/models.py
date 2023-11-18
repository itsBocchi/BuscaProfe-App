from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    especializacion = models.CharField(max_length=100)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=100)
    horarios = models.CharField(max_length=100)
    tarifas = models.DecimalField(max_digits=5, decimal_places=2)

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    correo = models.EmailField()
    contraseña = models.CharField(max_length=100)

    

# Create your models here.
