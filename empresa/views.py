from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Colaborador
from .models import Empresa
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

class EmpresaListado(ListView):
    model = Empresa

class ColaboradorListado(ListView):
    model = Colaborador # llama a la clase 'Colaborador' en 'models.py'

class ColaboradorCrear(SuccessMessageMixin, CreateView):
    model = Colaborador
    form = Colaborador # define el formulario con el nombre de la clase 'Colaborador'
    fields = "__all__" # muestra todos los campos de la tabla 'Colaborador'
    success_message = 'Colaborador Creado Correctamente'
    success_url = "./"

class ColaboradorDetalle(DetailView):
    model = Colaborador

class ColaboradorActualizar(SuccessMessageMixin, UpdateView):
    model = Colaborador
    form = Colaborador
    fields = "__all__"
    success_message = 'Actualización realizada correctamente'
    success_url = "../"

class ColaboradorEliminar(SuccessMessageMixin, DeleteView):
    model = Colaborador
    form = Colaborador
    success_message = 'Eliminación realizada correctamente'
    fields = "__all__"
    success_url = "../"

#Redireccionamos a la página principal luego de eliminar un registro o Colaborador
# def get_success_url(self):
#         success_message = 'Colaborador Eliminado Correctamente'
#         messages.success (self.request, (success_message))
#         return reverse('leer') # Redireccionamos a la vista principal 'leer'
