# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 04:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=100)),
                ('data', models.DateTimeField(default=datetime.datetime(2017, 7, 4, 0, 25, 11, 867605))),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='caixa',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caixa.Estado'),
        ),
    ]