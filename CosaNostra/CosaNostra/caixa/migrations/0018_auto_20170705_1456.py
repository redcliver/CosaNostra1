# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 18:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0017_auto_20170704_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 5, 14, 56, 7, 696235)),
        ),
    ]