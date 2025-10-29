from django.urls import path
from . import views

app_name='medico'

urlpatterns=[
   path('', views.Home_Medico,name='home_medico'), 
]