from django.shortcuts import render
from cortes.models import Atendimento
import datetime

# Create your views here.

def agenda(request):
    return render(request, 'agenda.html')

def agenda(request):
    if request.method == "GET":
        hoje = datetime.date.today()
        busca = Atendimento.objects.all().order_by('data').filter(data__icontains=hoje)
        return render(request, 'agenda.html', {'title':'Agenda', 'busca':busca})
    elif request.method == "POST":
        teste = request.POST.get('busca')
        busca = Atendimento.objects.all().order_by('data').filter(data__icontains=teste)
        return render(request, 'agenda.html', {'title':'Agenda', 'busca':busca})

