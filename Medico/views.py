from django.shortcuts import render, get_object_or_404
from P_Administrativo.models import CrearCita
from .models import Medico

# Create your views here.

def Home_Medico(request):
    return render(request,'home_medico.html')


def verCitas(request):
    medico=Medico.objects.get(user=request.user)
    citas=CrearCita.objects.filter(medico=medico)
    return render(request,'vercitas.html',{
        'citas':citas
    })

def detallecitas(request,cita_id):
    medico=Medico.objects.get(user=request.user)
    cita=get_object_or_404(CrearCita, id=cita_id, medico=medico)
    return render(request, 'detallescitas.html',{
        'cita':cita
    })
