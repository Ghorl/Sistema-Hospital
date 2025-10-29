from django.urls import path
from . import views

app_name='medico'

urlpatterns=[
   path('', views.Home_Medico,name='home_medico'), 
   path('vercitas/',views.verCitas,name='vercitas'),
   path('detalle_cita/<int:cita_id>',views.detallecitas,name='detallescita')
]