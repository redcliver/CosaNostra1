from django.shortcuts import render, HttpResponseRedirect
from .models import ClienteForm

# Create your views here.

def clientes(request):
    
    return render(request, 'clientes.html')

def addcliente(request):
    if request.method == "GET":
        form = ClienteForm()
        return render(request, 'addcliente.html', {'form':form})
    elif request.method == "POST":
        form = ClienteForm(request.POST)
        form.save()
        return HttpResponseRedirect('/home')