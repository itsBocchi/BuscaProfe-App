from django import forms
from .models import Profesor, Alumno

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'sexo', 'edad', 'especializacion', 'correo', 'contraseña', 'horarios', 'tarifas']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'