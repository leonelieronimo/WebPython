from asyncore import read
from modulefinder import IMPORT_NAME
from django.shortcuts import render
from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from AppWeb.models import Pancho, Hamburguesa, Pizza, Usuario
from AppWeb.forms import Formulario

def panchos(request):
    return render(request, "pancho.html", {})

def hamburguesa(request):
    return render(request, "hamburguesa.html", {})

def pizza(request):
    return render(request, "pizza.html", {})

def formulario(request):
    if request.method == 'POST':
        miFormulario = Formulario(request.POST)
        print(miFormulario)
    if miFormulario.is_valid():
        informacion = miFormulario.cleaned_data
        usuario = Usuario (nombre = informacion['nomCliente'], apellido = informacion['apellCliente'], dni = informacion['dni'])
        return render(request, "padre.html")
    else:
        miFormulario = Formulario()