# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-03 09:08
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import interpay.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interpay', '0016_auto_20161127_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('method', models.PositiveSmallIntegerField(choices=[(1, b'Debit'), (2, b'Credit')], default=1)),
                ('name', models.CharField(max_length=254)),
                ('account_id', models.BigIntegerField(default=interpay.models.make_id, primary_key=True, serialize=False)),
                ('when_opened', models.DateField(default=datetime.datetime.now, verbose_name='Date')),
                ('cur_code', models.CharField(default=b'IRR', max_length=3, verbose_name='cur_code')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='w_accounts', to=settings.AUTH_USER_MODEL)),
                ('spectators', models.ManyToManyField(related_name='r_accounts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cashing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('when', models.DateTimeField()),
                ('cur_code', models.CharField(default=b'USD', max_length=3, verbose_name='cur_code')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cashing_set', to='interpay.BankAccount')),
                ('banker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('when', models.DateTimeField(default=datetime.datetime.now)),
                ('cur_code', models.CharField(default=b'USD', max_length=3, verbose_name='cur_code')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_set', to='interpay.BankAccount')),
                ('banker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MoneyTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('total', models.FloatField()),
                ('comment', models.CharField(max_length=255)),
                ('cur_code', models.CharField(default=b'USD', max_length=3, verbose_name='cur_code')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_transfers', to='interpay.BankAccount')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcome_transfers', to='interpay.BankAccount')),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('cur_code', models.CharField(default=b'USD', max_length=3, verbose_name='cur_code')),
                ('deposit_charge_percent', models.FloatField(default=2)),
                ('credit_percent', models.FloatField(default=98)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 3, 12, 38, 42, 295000)),
        ),
    ]