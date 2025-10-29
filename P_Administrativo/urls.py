from django.urls import path
from . import views

app_name = 'p_Administrativo'

urlpatterns=[
    path('home_administracion/',views.Home,name='home_administrativo'),
    path('crear_citas/',views.view_CrearCitas, name='crear_citas'),
]