# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 19:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cortes', '0019_auto_20170705_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 5, 15, 42, 15, 666772)),
        ),
    ]
