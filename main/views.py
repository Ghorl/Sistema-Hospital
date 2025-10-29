from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.

def signin(request):
     if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
     else:
        # Autenticar usuario
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            # Iniciar sesión
           identificacion = user.username  # o user.dni si usas un campo personalizado

            # Redirigir según los primeros dígitos
           if identificacion.startswith('22'):
               return redirect('medico:home_medico')
           elif identificacion.startswith('33'):
               return redirect('p_administrativo:home_administrativo')
            
def signup(request):
    if request.method=='GET':
        return render(request, 'signup.html',{
        'form':UserCreationForm
        })
    else:
        if request.POST['password1']==request.POST['password2']:
             try:
                 user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                 user.save()
                 login(request,user)
                 return redirect('signin')
             except IntegrityError:
                  return render(request, 'signup.html',{
                         'form':UserCreationForm,
                          'error':'User already exists'
                    })
             
        return render(request, 'signup.html',{
                  'form':UserCreationForm,
                  'error':'Password do not match'
                 })
def signout(request):
    logout(request)
    return redirect('signin')