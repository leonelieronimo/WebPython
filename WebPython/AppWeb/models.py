from django.forms import CharField
from django.db import models

class Pancho(models.Model):
    agregado1 = models.CharField(max_length=15)
    agregado2 = models.CharField(max_length=15)
    agregado3 = models.CharField(max_length=15)
    bebida = models.CharField(max_length=10)
    guarnicion = models.CharField(max_length=20)
    nombreCliente = models.CharField(max_length=15)
    dni = models.IntegerField()

class Hamburguesa(models.Model):
    agregado1 = models.CharField(max_length=15)
    agregado2 = models.CharField(max_length=15)
    agregado3 = models.CharField(max_length=15)
    bebida = models.CharField(max_length=10)
    guarnicion = models.CharField(max_length=20)
    nombreCliente = models.CharField(max_length=15)
    dni = models.IntegerField()

class Pizza(models.Model):
    agregado1 = models.CharField(max_length=15)
    agregado2 = models.CharField(max_length=15)
    agregado3 = models.CharField(max_length=15)
    bebida = models.CharField(max_length=10)
    guarnicion = models.CharField(max_length=20)
    nombreCliente = models.CharField(max_length=15)
    dni = models.IntegerField()





