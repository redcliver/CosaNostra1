# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 21:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cortes', '0012_auto_20170704_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 17, 18, 45, 464491)),
        ),
    ]