from django.urls import path
from . import views

app_name='Medico'

urlpatterns=[
   path('', views.HelloWorld,name='home_medico'), 
]