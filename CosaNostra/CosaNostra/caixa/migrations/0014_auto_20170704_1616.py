# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 20:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0013_auto_20170704_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 16, 16, 14, 477227)),
        ),
    ]
