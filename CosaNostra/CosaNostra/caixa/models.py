from django.db import models
from django import forms
import datetime

# Create your models here.
class Caixa(models.Model):
    ESTADO_CHOICES = (
        (u'1', u'Aberto'),
        (u'2', u'Fechado'),
        )
    total = models.DecimalField(max_digits=100, decimal_places=2)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES)
    data = models.DateTimeField(default=datetime.datetime.now())
    
class caixaForm(forms.ModelForm):
    class meta:
        model = Caixa
        fields = ['total', 'estado', 'data']