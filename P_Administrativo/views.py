from django.shortcuts import render,redirect
from .forms import CreateNewCita
from .models import CrearCita

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
        # Cargar el formulario con los datos enviados
        form = CreateNewCita(request.POST)
        
        if form.is_valid():
            medico = form.cleaned_data['Medico']
            CrearCita.objects.create(
                medico=medico,
                paciente=f"{form.cleaned_data['N_Paciente']} {form.cleaned_data['A_Paciente']}",
                dni_paciente=form.cleaned_data['DNI_Paciente'],
                descripcion=form.cleaned_data['Descripcion'],
                fecha=form.cleaned_data['Fecha']
            )
            # Redirige al mismo formulario o a home, como prefieras
            return redirect('P_Administrativo:crear_citas')
        else:
            # Si hay errores, vuelve a mostrar el formulario con los mensajes
            return render(request, 'crearcitas.html', {
                'form': form
            })

       
       