from django.shortcuts import render, HttpResponseRedirect
from produto.models import  ProdutoForm
from outros.models import  ServicoForm

# Create your views here.
def outros(request):
    return render(request, 'outros.html', {'title':'Outros'})

def cadservico(request):
    if request.method == "GET":
        form = ServicoForm()
        return render(request, 'cadservico.html', {'title':'Cadastrar Serviço', 'form':form})
    elif request.method == "POST":
        form = ServicoForm(request.POST)
        form.save()
        form = ServicoForm()
        return render(request, 'cadservico.html', {'title':'Cadastrar Serviço', 'form':form})

def cadproduto(request):
    if request.method == "GET":
        form = ProdutoForm()
        return render(request, 'cadproduto.html', {'title':'Cadastrar produto', 'form':form})
    elif request.method == "POST":
        form = ProdutoForm(request.POST)
        form.save()
        form = ProdutoForm()
        return render(request, 'cadproduto.html', {'title':'Cadastrar produto', 'form':form})
    
    