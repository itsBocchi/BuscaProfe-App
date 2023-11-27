from django.urls import path
from .views import lista_profesor, dias_profesor, reservar_evento, todas_reservas
from .views import registro, iniciar_sesion, cerrar_sesion, home, crear_perfil, editar_perfil
from .views import perfil
from core import views

urlpatterns = [
    path('', home, name='home'),
    path('register/', registro, name='register'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    path('crear_perfil/', crear_perfil, name='crear_perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('perfil/<int:id_usuario>/', perfil, name='perfil'),
    path('profesores/', lista_profesor, name='lista_profesor'),
    path('profesores/<int:id_profesor>/days/', dias_profesor, name='dias_profesor'),
    path('reservar_evento/<int:correlativo>/', reservar_evento, name='reservar_evento'),
    path('todas_reservas/', todas_reservas, name='todas_reservas'),
    path('horario/', views.registrar_hora, name='horario'),
    path('ver/', views.hora, name='verhorario'),
]