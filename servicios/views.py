from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# // del segundo ejemplo que vimos traje estas lineas de código.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# hasta acá //

from .models import Servicio
from .models import CategoriaServicio
from .models import Usuario
from .models import Cliente
from .models import Empresa
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms


#def servicios(request):
    #servicios = CategoriaServicio.objects.all()
    #return render (request, 'base.html', {'servicios':servicios}))
    #return render (request, 'servicios/servicios_index.html', {'servicios':servicios})

class ServicioListado(LoginRequiredMixin, ListView):
    login_url = '/'
    model = Servicio
    def get_queryset(self):
        lista = []
        colaboradoresEmpresa = Usuario.objects.filter(Empresa=self.request.user.Empresa)
        for _colaborador in colaboradoresEmpresa:            
            serviciosColaborador = Servicio.objects.filter(colaborador=_colaborador)
            for servicio in serviciosColaborador:
                lista.append(servicio)
        return lista

class ServiciosCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/'
    model = Servicio
    form = Servicio
    fields = "__all__"
    success_message = 'Registro Creado Correctamente !'
    success_url = "./"

    def get_context_data(self, **kwargs):
        context = super(ServiciosCrear, self).get_context_data(**kwargs)
        context['form'].fields['colaborador'].queryset = Usuario.objects.filter(Empresa=self.request.user.Empresa).order_by('Nombre')
        context['form'].fields['cliente'].queryset = Cliente.objects.filter(Empresa=self.request.user.Empresa).order_by('Nombre')
        context['form'].fields['tipo_de_servicio'].queryset = CategoriaServicio.objects.filter(Empresa=self.request.user.Empresa).order_by('tipo_de_servicio')
        return context

class ServiciosActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/'
    model = Servicio
    form = Servicio
    fields = "__all__"
    success_message = 'Actualización realizada correctamente'
    success_url = "../"

class TipoServicioListado(LoginRequiredMixin, SuccessMessageMixin, ListView):
    login_url = '/'
    model = CategoriaServicio
    def get_queryset(self):
        lista = CategoriaServicio.objects.filter(Empresa=self.request.user.Empresa)
        lista = lista.order_by('tipo_de_servicio')
        return lista


class TipoServicioCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/'
    model = CategoriaServicio
    form = CategoriaServicio
    fields = ['tipo_de_servicio',]
    success_message = 'Servicio Creado Correctamente'
    success_url = "./"

    def form_valid(self, form):
        form.instance.Empresa = self.request.user.Empresa
        return super().form_valid(form)

class CategoriadeserviciosEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/'
    model = CategoriaServicio
    form = CategoriaServicio
    success_message = 'Eliminación realizada correctamente'
    fields = '__all__'
    success_url = "../"