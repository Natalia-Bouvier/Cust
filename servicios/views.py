from django.shortcuts import render

# Create your views here.
from .models import CategoriaServicio

def servicios(request):
    servicios = CategoriaServicio.objects.all()
    #return render (request, 'base.html', {'servicios':servicios}))
    return render (request, 'servicios/index.html', {'servicios':servicios})
