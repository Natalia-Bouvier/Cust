"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView #para usar RedirectView
from clientes.views import ClienteListado
from servicios.views import servicios
from empresa.views import EmpresaListado, ColaboradorListado, ColaboradorDetalle, ColaboradorCrear, ColaboradorActualizar, ColaboradorEliminar
from users import views
urlpatterns = [

    path('', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('',RedirectView.as_view(url='admin/', permanent=True)),
    # cuando accedes a la url principal te lleva a la carpeta que especifiques
    path('admin/', admin.site.urls),
    path('clientes/', ClienteListado.as_view(template_name="clientes/clientes_index.html"), name='leer'),
    path('servicios/',servicios),
    path('empresa/', EmpresaListado.as_view(template_name="empresa/empresa_index.html"), name='leer'),
    path('colaboradores/', ColaboradorListado.as_view(template_name="empresa/colaboradores_index.html"), name='leer'),
    # lista de los registros de colaboradores
    path('colaboradores/detalle/<int:pk>',ColaboradorDetalle.as_view(template_name = "empresa/colaboradores_detalles.html"), name='detalles'),
    # página que muestra los datos de un colaborador
    path('colaboradores/crear', ColaboradorCrear.as_view(template_name = "empresa/colaboradores_crear.html"), name='crear'),
    # formulario para crear un colaborador
    path('colaboradores/editar/<int:pk>', ColaboradorActualizar.as_view(template_name = "empresa/colaboradores_actualizar.html"), name='actualizar'),
    path('colaboradores/eliminar/<int:pk>', ColaboradorEliminar.as_view(), name='eliminar'),

]

#urlpatterns += staticfiles_urlpatterns()
