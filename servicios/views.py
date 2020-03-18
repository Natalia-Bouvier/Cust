from django.shortcuts import render

# // del segundo ejemplo que vimos traje estas lineas de código.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# hasta acá //

from .models import Servicio
from .models import CategoriaServicio
from .models import Colaborador
from .models import Cliente
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms


#def servicios(request):
    #servicios = CategoriaServicio.objects.all()
    #return render (request, 'base.html', {'servicios':servicios}))
    #return render (request, 'servicios/servicios_index.html', {'servicios':servicios})

class ServicioListado(ListView):
    model = Servicio

class ServiciosCrear(SuccessMessageMixin, CreateView):
    model = Servicio 
    form = Servicio 
    fields = "__all__"
    success_message = 'Registro Creado Correctamente !' 
    success_url = "./"
