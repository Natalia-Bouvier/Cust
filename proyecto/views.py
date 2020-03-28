from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        return render(request, '../templates/home.html')
    else:
        return redirect('/login')

def agenda(request):
    if request.user.is_authenticated:
        return render(request, '../templates/agenda.html')
    else:
        return redirect('/login')
def eventos(request):
    if request.user.is_authenticated:
        return render(request, '../templates/eventos.html')
    else:
        return redirect('/login')

def reservas(request):
    if request.user.is_authenticated:
        return render(request, '../templates/reservas.html')
    else:
        return redirect('/login')

def tareas(request):
    if request.user.is_authenticated:
        return render(request, '../templates/tareas.html')
    else:
        return redirect('/login')
