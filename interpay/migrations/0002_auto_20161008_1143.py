# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 08:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interpay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 8, 11, 43, 41, 867000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 8, 11, 43, 41, 867000)),
        ),
    ]
