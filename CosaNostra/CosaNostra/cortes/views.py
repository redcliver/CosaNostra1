from django.shortcuts import render, HttpResponseRedirect
from .models import ImediatoForm, AgendarForm

# Create your views here.

def cortes(request):
    return render(request, 'cortes.html', {'title':'Cortes'})

def imediato(request):
    if request.method == "GET":
        form = ImediatoForm()
        return render(request, 'imediato.html', {'title':'Imediato', 'form':form})
    elif request.method == "POST":
        form = ImediatoForm(request.POST)
        form.save()
        return HttpResponseRedirect('/home')

def agendar(request):
    form = AgendarForm()

    return render(request, 'agendar.html', {'title':'Agendar', 'form':form})