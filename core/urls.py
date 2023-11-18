from django.urls import path
from .views import registro, crear_perfil, iniciar_sesion, cerrar_sesion, home

urlpatterns = [
    path('register/', registro, name='register'),
    path('new_profile/', crear_perfil, name='new_profile'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    path('home/', home, name='home'),
    # Agrega otras URL según sea necesario
]