from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from .models import Colaborador
from .models import Empresa
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login as do_login
from empresa.forms import FormaRegistroEmpresa
from users.models import Usuario
from users.forms import FormaRegistro


class EmpresaDetalle(LoginRequiredMixin, DetailView):
    login_url = '/'
    model = Empresa

class ColaboradorListado(LoginRequiredMixin, ListView):
    login_url = '/'
    model = Usuario

    def get_queryset(self):
        lista = Usuario.objects.filter(Empresa=self.request.user.Empresa).filter(active=True)
        lista = lista.order_by('Nombre')
        return lista

#class ColaboradorCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#    login_url = '/'
#    model = Usuario
#    form = Usuario
#    fields = ['Nombre', 'fecha_nacimiento', 'direccion', 'sexo', 'telefono', 'correo', 'cedula', 'Observaciones',]
#    success_message = 'Colaborador Creado Correctamente'
#    success_url = "../"
#
#    def form_valid(self, form):
#        form.instance.Empresa = self.request.user.Empresa
#        form.instance.active = True
#        form.instance.staff = True
#        form.instance.admin = False
#        return super().form_valid(form)

class ColaboradorDetalle(LoginRequiredMixin, DetailView):
    login_url = '/'
    model = Usuario

class ColaboradorActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/'
    model = Usuario
    form = Usuario
    fields = ['Nombre', 'fecha_nacimiento', 'direccion', 'sexo', 'telefono', 'correo', 'cedula', 'Observaciones',]
    success_message = 'Actualización realizada correctamente'
    success_url = "../"

class ColaboradorEliminar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/'
    model = Usuario
    form = Usuario
    fields = []
    success_message = 'Se elimino correctamente el colaborador.'
    success_url = "../"
   
    def form_valid(self, form):
        form.instance.active = False
        return super().form_valid(form)


def crear(request):
    # Creamos el formulario de autenticación vacío
    form = FormaRegistro()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = FormaRegistro(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save(request)

            # Si el usuario se crea correctamente
            if user is not None:
                # Y le redireccionamos a la portada
                return redirect('../')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/register.html", {'form': form})

def registro_empresa(request):
    # Creamos el formulario de autenticación vacío
    if not request.user.is_authenticated:
        return redirect('/')
    if request.user.Empresa is not None:
        return redirect('/')

    form = FormaRegistroEmpresa()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = FormaRegistroEmpresa(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            empresa = form.save()

            # Si el usuario se crea correctamente
            if empresa is not None:
                # Hacemos el login manualmente
                request.user.Empresa = empresa
                request.user.save()
                # Y le redireccionamos a la portada
                return redirect('/')

    return render(request, "empresa/registro_empresa.html", {'form': form})

#Redireccionamos a la página principal luego de eliminar un registro o Colaborador
# def get_success_url(self):
#         success_message = 'Colaborador Eliminado Correctamente'
#         messages.success (self.request, (success_message))
#         return reverse('leer') # Redireccionamos a la vista principal 'leer'
