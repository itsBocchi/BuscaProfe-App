from django.contrib import admin
from .models import Day, Event, Reserva, Hora, Categoria

admin.site.register(Day)

admin.site.register(Event)

admin.site.register(Reserva)


admin.site.register(Categoria)
admin.site.register(Hora)