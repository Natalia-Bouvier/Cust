from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cliente
from empresa.models import Empresa
from servicios.models import Servicio
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

class ClienteListado(LoginRequiredMixin, ListView):
    login_url = '/'
    model = Cliente

class ClienteCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/'
    model = Cliente
    form = Cliente
    fields = "__all__"
    success_message = 'Cliente Creado Correctamente'
    success_url = "./"

class ClienteDetalle(LoginRequiredMixin, DetailView):
    login_url = '/'
    model = Cliente

class ClienteActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/'
    model = Cliente
    form = Cliente
    fields = "__all__"
    success_message = 'Actualización realizada correctamente'
    success_url = "../"

class ClienteEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/'
    model = Cliente
    form = Cliente
    success_message = 'Eliminación realizada correctamente'
    fields = "__all__"
    success_url = "../"
