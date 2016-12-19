# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-19 12:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interpay', '0020_auto_20161219_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='cur_code',
            field=models.CharField(default=b'RLS', max_length=3, verbose_name='cur_code'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 19, 16, 27, 39, 542000)),
        ),
    ]
