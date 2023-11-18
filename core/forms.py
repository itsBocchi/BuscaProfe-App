from django import forms
from .models import Event, Reserva

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_time', 'end_time', 'day']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['opcion', 'dato_extra']
