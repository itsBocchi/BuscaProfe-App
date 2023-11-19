from django.urls import path
from .views import lista_profesor, dias_profesor, reservar_evento, todas_reservas
from .views import Registro, Iniciar_Sesion, Cerrar_Sesion, home, crear_Perfil, editar_Perfil

urlpatterns = [
    path('', home, name='home'),
    path('register/', Registro, name='register'),
    path('login/', Iniciar_Sesion, name='login'),
    path('logout/', Cerrar_Sesion, name='logout'),
    path('crear_perfil/', crear_Perfil, name='crear_perfil'),
    path('editar_perfil/', editar_Perfil, name='editar_perfil'),
    path('profesores/', lista_profesor, name='lista_profesor'),
    path('profesores/<int:id_profesor>/days/', dias_profesor, name='dias_profesor'),
    path('reservar_evento/<int:event_id>/', reservar_evento, name='reservar_evento'),
    path('todas_reservas/', todas_reservas, name='todas_reservas'),
]