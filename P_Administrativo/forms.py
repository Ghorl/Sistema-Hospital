from django import forms
from Medico.models import Medico

class CreateNewCita(forms.Form):
    N_Paciente=forms.CharField(label="Nombre de Paciente", max_length=20,)
    A_Paciente = forms.CharField(label="Apellido de Paciente", max_length=20)
    DNI_Paciente = forms.CharField(label="DNI del Paciente", max_length=8)
    Descripcion = forms.CharField(widget=forms.Textarea, label="Descripción")
    Fecha=forms.DateTimeField(label="Fecha de Cita", widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    Medico=forms.ModelChoiceField(queryset=Medico.objects.all(),
        label="Asignar a Médico")

