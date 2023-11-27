from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User


class Day(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=10, choices=[('profesor', 'Profesor'), ('alumno', 'Alumno')])
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Event(models.Model):
    profesor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Reserva(models.Model):
    opcion = models.CharField(max_length=10, choices=[('presencial', 'Presencial'), ('online', 'Online')])
    dato_extra = models.TextField()
    evento = models.ForeignKey(Event, on_delete=models.CASCADE)
    completada = models.BooleanField(default=False)
    def __str__(self):
        return f"Reserva para {self.evento.name}" if self.evento else "Reserva sin evento"
    
    # almacena comentarios de un usuario en el perfil de otro usuario
class ComentarioPerfil(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autor')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinatario')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Comentario de {self.autor.username} a {self.destinatario.username}"




class Categoria(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Hora(models.Model):

    """
    Modelo para representar las categorías de los comunicados.

    - nombre: Campo de texto para el nombre de la categoría.
    - descripcion: Campo de texto para la descripción de la categoría.
    """

    HORA_CHOICES = [
        ("001", "08:00 - 08:45"),
("002", "08:45 - 09:30"),
("003", "09:30 - 10:15"),
("004", "10:15 - 11:00"),
("005", "11:00 - 11:45"),
("006", "11:45 - 12:30"),
("007", "12:30 - 13:15"),
("008", "13:15 - 14:00"),
("009", "14:00 - 14:45"),
("010", "14:45 - 15:30"),
("011", "15:30 - 16:15"),
("012", "16:15 - 17:00"),
("013", "17:00 - 17:45"),
("014", "17:45 - 18:30"),
("015", "18:30 - 19:15"),
("016", "19:15 - 20:00"),


    ]

    correlativo = models.AutoField(primary_key=True)
    titulo = models.TextField()
    detalle = models.TextField()
    nivel = models.TextField(choices=HORA_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    dia = models.ForeignKey(Day, on_delete=models.CASCADE, null=True)
    reserva = models.OneToOneField('Reserva', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo

    def __str__(self):
        return f"{self.nivel}: {self.titulo}"
