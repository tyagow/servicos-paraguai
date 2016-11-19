# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimento',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='estabelecimento',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]