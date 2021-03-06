# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-22 12:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interpay', '0014_auto_20161115_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerificationCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_code', models.IntegerField(max_length=6)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 22, 15, 48, 54, 713000)),
        ),
        migrations.AddField(
            model_name='verificationcodes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verif_code_user', to='interpay.UserProfile'),
        ),
    ]
