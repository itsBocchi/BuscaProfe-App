from django.urls import path
from .views import Registro, Iniciar_Sesion, Cerrar_Sesion, home

urlpatterns = [
    path('register/', Registro, name='register'),
    path('login/', Iniciar_Sesion, name='login'),
    path('logout/', Cerrar_Sesion, name='logout'),
    path('home/', home, name='home'),
    # Agrega otras URL según sea necesario
]