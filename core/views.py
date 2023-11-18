from datetime import datetime, timedelta
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Teacher, Day, Event, Reserva
from .forms import ReservaForm
from django.contrib import messages

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'core/profesores.html', {'teachers': teachers})

def teacher_days(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    days = Day.objects.all()
    events = Event.objects.filter(teacher=teacher)
    events_by_day = {day: events.filter(day=day) for day in days}

    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    formatted_start_of_week = start_of_week.strftime('%Y-%m-%d')

    context = {
        'teacher': teacher,
        'days': days,
        'events_by_day': events_by_day,
        'formatted_start_of_week': formatted_start_of_week,
    }

    return render(request, 'core/profesor_dias.html', context)

def todas_reservas(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'core/eventos.html', context)

def reservar_evento(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva_existente = Reserva.objects.filter(evento=event)
            if reserva_existente.exists():
                messages.error(request, 'Este evento ya ha sido reservado.')
                return redirect('todas_reservas')

            reserva = form.save(commit=False)
            reserva.evento = event
            reserva.save()

            event.completada = True
            event.save()

            return redirect('todas_reservas')
    else:
        form = ReservaForm(initial={'evento': event})

    context = {'form': form, 'event': event}
    return render(request, 'core/reservar.html', context)