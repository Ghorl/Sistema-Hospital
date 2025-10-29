
# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    numero_colegiatura = models.CharField(max_length=50)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} - {self.especialidad}"
