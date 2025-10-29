from django.shortcuts import render,redirect
from .forms import CreateNewCita
from .models import CrearCita
from Medico.models import Medico

# Create your views here.
def Home(request):
  return render(request, 'home_administrativo.html')

def view_CrearCitas(request):
    if request.method == 'GET':
        # Mostrar el formulario vacío
        return render(request, 'crearcitas.html', {
            'form': CreateNewCita()
        })
    else:
        medio_id=request.POST.get('Medico')
        medico=Medico.objects.get(id=medio_id)
        CrearCita.objects.create(
            medico=medico,
            paciente=f"{request.POST['N_Paciente']} {request.POST['A_Paciente']}",
            dni_paciente=request.POST['DNI_Paciente'],
            descripcion=request.POST['Descripcion'],
            fecha=request.POST['Fecha']
        )
        return redirect('p_administrativo:crear_citas')

       
       