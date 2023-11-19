from django import forms
from .models import Event, Reserva, UserProfile, ComentarioPerfil

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_time', 'end_time', 'day']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['opcion', 'dato_extra']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['tipo_usuario', 'nombre', 'apellido', 'telefono', 'email']

class ComentarioPerfilForm(forms.ModelForm):
    class Meta:
        model = ComentarioPerfil
        fields = ['texto']