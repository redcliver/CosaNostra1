# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 03:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0023_auto_20170705_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 5, 23, 38, 43, 50580)),
        ),
    ]
