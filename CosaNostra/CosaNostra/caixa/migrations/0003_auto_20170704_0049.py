# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 04:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0002_auto_20170704_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 0, 49, 26, 134374)),
        ),
    ]
