from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
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
