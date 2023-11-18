from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.forms import UserProfileForm
from core.models import UserProfile

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'core/home.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('new_profile')  
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
