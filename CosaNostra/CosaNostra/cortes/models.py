from django.db import models
from django import forms
from clientes.models import Cliente
from caixa.models import Caixa
from outros.models import Servico

import datetime

# Create your models here.

class Atendimento(models.Model):
    data = models.DateTimeField(default=datetime.datetime.now())
    cliente = models.ForeignKey(Cliente)
    servico = models.ForeignKey(Servico)
    
   

class ImediatoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['cliente','servico']
        exclude = ['data']

class AgendarForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['cliente','servico', 'data']