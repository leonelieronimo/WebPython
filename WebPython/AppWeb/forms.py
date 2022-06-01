from django import forms

class Formulario(forms.Form):
    nomCliente = forms.CharField(max_length=15)
    apellCliente = forms.CharField(max_length=20)
    dni = forms.IntegerField()
