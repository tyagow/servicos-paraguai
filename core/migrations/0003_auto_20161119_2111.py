# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20161119_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='estabelecimento',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=7, null=True),
        ),
    ]
