from django.db import models
from django import forms

# Create your models here.
class Servico(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.nome

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'preco', 'descricao']