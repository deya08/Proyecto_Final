from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
#from apps.perfil.forms import RegistroForm
# Create your views here.



def index(request):
	return render(request, "inicio/index.html")

def registrado(request):
	return render(request, "inicio/registrado.html")

def registro(request):
	return render(request, "inicio/registro.html")


"""class RegistroUsuario(CreateView):
	model= User
	template_name= 'inicio/registro.html'
	form_class= RegistroForm
	success_url= reverse_lazy('index')"""