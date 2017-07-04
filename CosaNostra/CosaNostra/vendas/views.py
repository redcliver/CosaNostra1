from django.shortcuts import render

# Create your views here.

def vendas(request):
    return render(request, 'vendas.html')