from django.urls import path
from . import views

app_name='Administracion'

urlpatterns=[
    path('crear_citas/',views.view_CrearCitas, name='crear_citas'),
    path('home_administracion/',views.Home,name='home_administrativo'),
]