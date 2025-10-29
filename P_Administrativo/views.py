from django.shortcuts import render
from .models import CrearCitas

# Create your views here.
def Home(request):
  return render(request, 'home_administrativo.html')

def view_CrearCitas(request):
  