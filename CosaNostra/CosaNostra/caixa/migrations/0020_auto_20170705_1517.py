# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 19:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0019_auto_20170705_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 5, 15, 17, 14, 284827)),
        ),
    ]