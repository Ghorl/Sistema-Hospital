from django.shortcuts import render

# Create your views here.

def HelloWorld(request):
    return render(request,'home_medico.html')
