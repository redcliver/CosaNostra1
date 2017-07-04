from django.db import models
from django import forms

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    tel = models.IntegerField()
    dataNasc = models.DateField()

    def __str__(self):
        return self.nome
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente;
        fields = ['nome', 'tel', 'dataNasc']