# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 19:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0007_auto_20170704_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 15, 54, 39, 554907)),
        ),
    ]
