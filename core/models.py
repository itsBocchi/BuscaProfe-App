from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Day(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.is_profesor and not hasattr(self, 'profesor'):
            Profesor.objects.create(usuario=self.user)

        if self.is_estudiante and not hasattr(self, 'estudiante'):
            Estudiante.objects.create(usuario=self.user)
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50, default='obamna@usa.soda')
    especialidad = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50, default='obamna@usa.soda')
    descripcion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()