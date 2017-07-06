from django.shortcuts import render, HttpResponseRedirect
from .models import Atendimento ,ImediatoForm, AgendarForm
from caixa.models import Caixa
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
        form = ImediatoForm()
        credito = Atendimento.objects.latest('pk')
        caixa = Caixa.objects.latest('pk')
        creditoTotal = caixa.total+credito.servico.preco
        fechamento = Caixa(estado=1, total=creditoTotal)
        fechamento.save()
        return render(request, 'imediato.html', {'title':'Imediato', 'form':form})

def agendar(request):
    if request.method == "GET":
        form = AgendarForm()
        return render(request, 'agendar.html', {'title':'Agendar', 'form':form})
    elif request.method == "POST":
        form = AgendarForm(request.POST)
        form.save()
        form = AgendarForm()
        
        return render(request, 'agendar.html', {'title':'Agendar', 'form':form})