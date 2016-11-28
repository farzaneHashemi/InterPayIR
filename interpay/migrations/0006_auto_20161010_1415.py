# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 10:45
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interpay', '0005_auto_20161010_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 10, 14, 15, 16, 176000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='national_code',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(b'^[0-9]*$', b'Only numeric characters are allowed.')]),
        ),
    ]