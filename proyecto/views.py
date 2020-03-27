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

    
