from django.shortcuts import render
from caixa.models import Caixa, caixaForm
# Create your views here.


def caixa(request):
    total = Caixa.objects.latest('id')
    return render(request, 'caixa.html',{'total':total, 'title':'Caixa'})
   