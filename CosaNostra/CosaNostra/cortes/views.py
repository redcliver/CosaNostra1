from django.shortcuts import render

# Create your views here.

def cortes(request):
    return render(request, 'cortes.html')

def imediato(request):
    return render(request, 'imediato.html')

def agendar(request):
    return render(request, 'agendar.html')