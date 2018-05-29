from django.urls import path
from apps.perfil.views import *
#from apps.perfil.views import *


app_name="perfil"

urlpatterns = [
  path('', index, name='index'),
  path('registrado/', registrado, name='registrado'),
  path('registro/', registro, name='registro')
]
