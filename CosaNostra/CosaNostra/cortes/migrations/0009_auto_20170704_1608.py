# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 20:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cortes', '0008_auto_20170704_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendimento',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='atendimento',
            name='servico',
        ),
        migrations.DeleteModel(
            name='Atendimento',
        ),
    ]