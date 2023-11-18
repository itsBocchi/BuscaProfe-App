from django.shortcuts import render, redirect
from .models import Profesor, Alumno
from .forms import ProfesorForm, AlumnoForm

def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perfil_profesor')
    else:
        form = ProfesorForm()
    return render(request, 'crear_profesor.html', {'form': form})

def editar_profesor(request):
    profesor = Profesor.objects.first()  # Obtén el profesor a editar
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('perfil_profesor')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'editar_profesor.html', {'form': form})

def perfil_profesor(request):
    profesor = Profesor.objects.first()  # Obtén el profesor a mostrar
    return render(request, 'perfil_profesor.html', {'profesor': profesor})

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perfil_alumno')
    else:
        form = AlumnoForm()
    return render(request, 'perfil/crear_perfil_alumno.html', {'form': form})


def perfil_alumno(request):
    alumnos = Alumno.objects.all()
    return render(request, 'perfil/perfil_alumno.html', {'alumnos': alumnos})
# Vistas similares para crear, editar y mostrar el perfil del alumno
# Create your views here.
