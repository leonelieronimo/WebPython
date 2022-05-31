from asyncore import read
from modulefinder import IMPORT_NAME
from django.shortcuts import render
from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from AppWeb.models import Pancho, Hamburguesa, Pizza

def panchos(request):
    return render(request, "pancho.html", {})

def hamburguesa(request):
    return render(request, "hamburguesa.html", {})

def pizza(request):
    return render(request, "pizza.html", {})
