from django.shortcuts import render, redirect
from .forms import ProfesorForm, AlumnoForm
from .models import Profesor, Alumno

def crear_perfil_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perfil_profesor')
    else:
        form = ProfesorForm()
    return render(request, 'crear_perfil_profesor.html', {'form': form})

def perfil_profesor(request):
    profesor = Profesor.objects.all() 
    return render(request, 'perfil_profesor.html', {'profesor': profesor})

def crear_perfil_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perfil_alumno')
    else:
        form = AlumnoForm()
    return render(request, 'crear_perfil_alumno.html', {'form': form})

def perfil_alumno(request):
    alumno = Alumno.objects.all() 
    return render(request, 'perfil_alumno.html', {'alumno': alumno})