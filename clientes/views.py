from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cliente

# def clientes(request):
#     clientes = Cliente.objects.all()
#     #Cliente_list = "- ".join([str(Cliente) for Cliente in clientes])
#     #return HttpResponse(Cliente_list)
#     return render (request, 'clientes/Cliente_list.html', {'clientes':clientes})
#
# def prueba(request):
#     return HttpResponse("PruebaFer")

class ClienteListado(ListView):
    model = Cliente
