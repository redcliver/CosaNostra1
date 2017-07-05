from django.shortcuts import render
from produto.models import Produto,ProdutoForm
from caixa.models import Caixa
from .models import Vendas ,ImediatoForm

# Create your views here.

def vendas(request):
    return render(request, 'vendas.html', {'title':'Vendas'})

def imediato(request):
    if request.method == "GET":
        form = ImediatoForm()
        return render(request, 'imediato.html', {'title':'Imediato', 'form':form})
    elif request.method == "POST":
        form = ImediatoForm(request.POST)
        form.save()
        form = ImediatoForm()
        credito = Vendas.objects.latest('pk')
        caixa = Caixa.objects.latest('pk')
        creditoTotal = caixa.total+credito.produto.preco
        fechamento = Caixa(estado=1, total=creditoTotal)
        fechamento.save()
        return render(request, 'imediato.html', {'title':'Imediato', 'form':form})

def bar(request):
    return render(request, 'bar.html', {'title':'Bar'})