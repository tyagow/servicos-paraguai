# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-17 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import src.core.utils


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20170715_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='logo',
            field=models.ImageField(help_text='### ATENÇÃO - TAMANHO DA IMAGEM PRECISA SER 310x294 ###', null=True, upload_to=src.core.utils.path_and_rename_logo),
        ),
        migrations.AlterField(
            model_name='foto',
            name='foto',
            field=models.ImageField(blank=True, help_text='### ATENÇÃO - TAMANHO DA IMAGEM PRECISA SER 800x800 ###', null=True, upload_to=src.core.utils.path_and_rename_fotos),
        ),
    ]