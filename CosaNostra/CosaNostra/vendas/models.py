from django.db import models
from django import forms
from clientes.models import Cliente
from produto.models import Produto
import datetime

# Create your models here.

class Vendas(models.Model):
    data = models.DateTimeField(default=datetime.datetime.now())
    cliente = models.ForeignKey(Cliente)
    produto = models.ForeignKey(Produto)
    quantidade = models.IntegerField()
    
class ImediatoForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ['cliente','produto', 'quantidade']
        exclude = ['data']