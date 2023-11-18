from django.urls import path
from .views import teacher_list, teacher_days, reservar_evento, todas_reservas

urlpatterns = [
    path('profesores/', teacher_list, name='teacher_list'),
    path('profesores/<int:teacher_id>/days/', teacher_days, name='teacher_days'),
    path('reservar_evento/<int:event_id>/', reservar_evento, name='reservar_evento'),
    path('todas_reservas/', todas_reservas, name='todas_reservas'),
]