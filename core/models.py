from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Day(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
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
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega cualquier campo adicional que necesites para tu usuario

    def __str__(self):
        return self.user.username
