# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 20:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0012_auto_20170704_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 16, 9, 55, 687869)),
        ),
    ]
