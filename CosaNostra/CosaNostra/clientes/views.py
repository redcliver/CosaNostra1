from django.shortcuts import render, HttpResponseRedirect
from .models import  Cliente, ClienteForm

# Create your views here.

def clientes(request):
    
    return render(request, 'clientes.html', {'title':'Clientes'})

def addcliente(request):
    if request.method == "GET":
        form = ClienteForm()
        return render(request, 'addcliente.html', {'title':'Adicionar cliente', 'form':form})
    elif request.method == "POST":
        form = ClienteForm(request.POST)
        form.save()
        form = ClienteForm()
        return render(request, 'addcliente.html', {'title':'Adicionar cliente', 'form':form})

def buscacli(request):
    if request.method == "GET":
        return render(request, 'buscaCli.html', {'title':'Buscar cliente'})
    elif request.method == "POST":
        teste = request.POST.get('busca')
        busca = Cliente.objects.all().filter(nome__contains=teste).values('nome', 'tel', 'dataNasc')
        return render(request, 'buscaCli.html', {'title':'Buscar cliente', 'busca':busca})
        