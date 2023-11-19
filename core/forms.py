from django import forms
from .models import Event, Reserva, UserProfile

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