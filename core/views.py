from datetime import datetime, timedelta
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from .models import UserProfile, Day, Event, Reserva, ComentarioPerfil, Categoria, Hora
from .forms import ReservaForm, UserProfileForm, ComentarioPerfilForm, HoraForm
from django.utils import timezone

def lista_profesor(request):
    profesores = UserProfile.objects.filter(tipo_usuario='profesor')

    return render(request, 'core/profesores.html', {'profesores': profesores})

from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import UserProfile, Day, Event, Reserva, ComentarioPerfil, Categoria, Hora
from .forms import ReservaForm, UserProfileForm, ComentarioPerfilForm, HoraForm
from django.utils import timezone

def dias_profesor(request, id_profesor):
    profesor = get_object_or_404(UserProfile, id=id_profesor)
    days = Day.objects.all()
    horarios = Hora.objects.filter(publicado_por=profesor.user)
    horarios_by_day = {day: horarios.filter(dia=day) for day in days}

    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    formatted_start_of_week = start_of_week.strftime('%Y-%m-%d')

    context = {
        'profesor': profesor,
        'days': days,
        'horarios_by_day': horarios_by_day,
        'formatted_start_of_week': formatted_start_of_week,
    }

    return render(request, 'core/profesor_dias.html', context)


def todas_reservas(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'core/eventos.html', context)

def reservar_evento(request, correlativo):
    horario = get_object_or_404(Hora, correlativo=correlativo)

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva_existente = horario.reserva
            if reserva_existente:
                # Manejar el caso en que el horario ya tiene una reserva
                # Puedes redirigir a otra página o mostrar un mensaje de error
                pass
            else:
                reserva = form.save(commit=False)
                reserva.horario = horario
                reserva.save()

                horario.reserva = reserva
                horario.save()

                return render(request, 'profesores/.html')  # Reemplaza con la página que desees mostrar después de una reserva exitosa
    else:
        form = ReservaForm()

    context = {'form': form, 'horario': horario}
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





def hora(request):

    """
    Vista para mostrar la página principal que lista todos los comunicados.

    - Obtiene todos los comunicados.
    - Filtra por nivel si se especifica.
    - Filtra por categoría si se especifica.
    - Obtiene todas las categorías.

    Retorna la respuesta renderizada con el contexto en la plantilla 'comunicados/index.html'.
    """

    comunicados = Hora.objects.all()
    nivel = request.GET.get('nivel')
    categoria_id = request.GET.get('categoria')
    day_id = request.GET.get('day')

    selected_day = None
    if day_id:
        selected_day = Day.objects.get(id=day_id)

    if nivel:
        comunicados = comunicados.filter(nivel=nivel)

    if categoria_id:
        categoria = Categoria.objects.get(id=categoria_id)
        comunicados = comunicados.filter(categoria=categoria)

    if day_id:
        comunicados = comunicados.filter(day_id=day_id)

    categorias = Categoria.objects.all()
    days = Day.objects.all()

    context = {
        'comunicados': comunicados,
        'categorias': categorias,
        'days': days,
        'selected_day': selected_day,
    }
    return render(request, 'horario/verhorario.html', context)


@login_required
def registrar_hora(request):
    """
    Vista para registrar un nuevo comunicado.
    
    - Obtiene la fecha actual.
    - Si el método de solicitud es POST, procesa el formulario enviado y guarda el comunicado.
    - Si el método de solicitud es GET, muestra el formulario de registro de comunicado.
    
    Retorna la respuesta renderizada con el contexto en la plantilla 'comunicados/registrar_comunicado.html'.
    """
    fecha_actual = timezone.now().date()
    
    if request.method == 'POST':
        form = HoraForm(request.POST)
        if form.is_valid():
            comunicado = form.save(commit=False)
            comunicado.publicado_por = request.user
            comunicado.save()
            messages.success(request, 'Comunicado registrado exitosamente.')
            return redirect('verhorario')
    else:
        form = HoraForm()
    
    context = {
        'fecha_actual': fecha_actual,
        'form': form,
    }
    return render(request, 'horario/horario.html', context)

