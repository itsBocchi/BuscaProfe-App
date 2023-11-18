from django.urls import path
from .views import teacher_list, teacher_days, reservar_evento, todas_reservas
from .views import Registro, Iniciar_Sesion, Cerrar_Sesion, home

urlpatterns = [
    path('profesores/', teacher_list, name='teacher_list'),
    path('profesores/<int:teacher_id>/days/', teacher_days, name='teacher_days'),
    path('reservar_evento/<int:event_id>/', reservar_evento, name='reservar_evento'),
    path('todas_reservas/', todas_reservas, name='todas_reservas'),
    path('register/', Registro, name='register'),
    path('login/', Iniciar_Sesion, name='login'),
    path('logout/', Cerrar_Sesion, name='logout'),
    path('home/', home, name='home'),
]