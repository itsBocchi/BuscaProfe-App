from datetime import datetime, timedelta
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages, get_object_or_404, redirect, HttpResponse
from .models import Teacher, Day, Event, Reserva
from .forms import ReservaForm
from django.contrib import messages

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'core/profesores.html', {'teachers': teachers})

def teacher_days(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    days = Day.objects.all()
    events = Event.objects.filter(teacher=teacher)
    events_by_day = {day: events.filter(day=day) for day in days}

    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    formatted_start_of_week = start_of_week.strftime('%Y-%m-%d')

    context = {
        'teacher': teacher,
        'days': days,
        'events_by_day': events_by_day,
        'formatted_start_of_week': formatted_start_of_week,
    }

    return render(request, 'core/profesor_dias.html', context)

def todas_reservas(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'core/eventos.html', context)

def reservar_evento(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva_existente = Reserva.objects.filter(evento=event)
            if reserva_existente.exists():
                messages.error(request, 'Este evento ya ha sido reservado.')
                return redirect('todas_reservas')

            reserva = form.save(commit=False)
            reserva.evento = event
            reserva.save()

            event.completada = True
            event.save()

            return redirect('todas_reservas')
    else:
        form = ReservaForm(initial={'evento': event})

    context = {'form': form, 'event': event}
    return render(request, 'core/reservar.html', context)
def home(request):
    return render(request, 'core/home.html')

def Registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Reemplaza 'home' con la URL a la que quieres redirigir después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def Iniciar_Sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Reiniciar el contador de intentos después de un inicio de sesión exitoso
            request.session['incorrect_attempts'] = 0

            return redirect('home')  # Reemplaza 'home' con la URL a la que quieres redirigir después del inicio de sesión
        else:
            # Contar el número de intentos de inicio de sesión incorrectos
            username = request.POST.get('username', '')
            incorrect_attempts = request.session.get('incorrect_attempts', 0)
            incorrect_attempts += 1
            request.session['incorrect_attempts'] = incorrect_attempts

            if incorrect_attempts >= 5:
                messages.error(request, 'Demasiados intentos fallidos. Por favor, inténtalo más tarde.')
            else:
                messages.error(request, 'Intento {}/5'.format(incorrect_attempts))
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def Cerrar_Sesion(request):
    logout(request)
    return redirect('login')  # Reemplaza 'login' con la URL a la que quieres redirigir después de cerrar sesión
