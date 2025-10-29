from django.db import models
from Medico.models import Medico

class CrearCita(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.CharField(max_length=100)
    dni_paciente = models.CharField(max_length=8)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"Cita con {self.medico} el {self.fecha.strftime('%d/%m/%Y %H:%M')}"
