# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cortes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='data',
            field=models.DateTimeField(default='04/07/2017 15:23'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outros.Servico'),
        ),
    ]
