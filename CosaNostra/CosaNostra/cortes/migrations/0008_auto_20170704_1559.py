# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cortes', '0007_auto_20170704_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='data',
            field=models.DateTimeField(default='04/07/2017 15:59'),
        ),
    ]
