from django.db import models
from django.contrib.auth.models import User


class Day(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
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
