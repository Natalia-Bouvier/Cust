from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cliente
from empresa.models import Empresa
from servicios.models import Servicio
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

class ClienteListado(ListView):
    model = Cliente

class ClienteCrear(SuccessMessageMixin, CreateView):
    model = Cliente
    form = Cliente # define el formulario con el nombre de la clase 'Cliente'
    fields = "__all__" # muestra todos los campos de la tabla 'Cliente'
    success_message = 'Cliente Creado Correctamente'
    success_url = "./"

class ClienteDetalle(DetailView):
    model = Cliente

class ClienteActualizar(SuccessMessageMixin, UpdateView):
    model = Cliente
    form = Cliente
    fields = "__all__"
    success_message = 'Actualización realizada correctamente'
    success_url = "../"

class ClienteEliminar(SuccessMessageMixin, DeleteView):
    model = Cliente
    form = Cliente
    success_message = 'Eliminación realizada correctamente'
    fields = "__all__"
    success_url = "../"