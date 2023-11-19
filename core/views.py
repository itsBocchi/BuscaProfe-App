from datetime import datetime, timedelta
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from .models import UserProfile, Day, Event, Reserva, ComentarioPerfil
from .forms import ReservaForm, UserProfileForm, ComentarioPerfilForm

def lista_profesor(request):
    profesores = UserProfile.objects.filter(tipo_usuario='profesor')

    return render(request, 'core/profesores.html', {'profesores': profesores})

def dias_profesor(request, id_profesor):
    profesor = get_object_or_404(UserProfile, id=id_profesor)
    days = Day.objects.all()
    events = Event.objects.filter(profesor=profesor)
    events_by_day = {day: events.filter(day=day) for day in days}

    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    formatted_start_of_week = start_of_week.strftime('%Y-%m-%d')

    context = {
        'profesor': profesor,
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
    if not request.user.is_authenticated:
         return redirect('login')
    return render(request, 'core/home.html', {'tipo_usuario': request.user.userprofile.tipo_usuario})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('crear_perfil')  # Reemplaza 'home' con la URL a la que quieres redirigir después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def crear_perfil(request):
    # Verificar si el perfil ya existe para el usuario actual
    try:
        perfil_existente = request.user.userprofile
        return redirect('perfil_existente')  # Redirigir a una página que informa que el perfil ya existe
    except UserProfile.DoesNotExist:
        pass

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.user = request.user
            perfil.save()
            return redirect('seleccionar_tipo_perfil')
    else:
        form = UserProfileForm()

    return render(request, 'crear_perfil.html', {'form': form})

def iniciar_sesion(request):
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

def cerrar_sesion(request):
    logout(request)
    return redirect('login')  # Reemplaza 'login' con la URL a la que quieres redirigir después de cerrar sesión

def crear_perfil(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('home')
    else:
        form = UserProfileForm()

    return render(request, 'registration/crear_perfil.html', {'form': form})


def editar_perfil(request):
    
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()

            return redirect('perfil', id_usuario=request.user.id)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'registration/editar_perfil.html', {'form': form})

def perfil(request, id_usuario):
    user_profile = get_object_or_404(UserProfile, user_id=id_usuario)
    ubicacion_perfil = 'core/perfil.html'  # Remove extra indentation here

    if request.method == 'POST':
        form = ComentarioPerfilForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.destinatario = user_profile.user
            comentario.save()
            return redirect('perfil', id_usuario=id_usuario)
    else:
        form = ComentarioPerfilForm()

    comentarios = ComentarioPerfil.objects.filter(destinatario=user_profile.user)
    context = {'comentarios': comentarios, 'form': form, 'user_profile': user_profile}
    return render(request, ubicacion_perfil, context)