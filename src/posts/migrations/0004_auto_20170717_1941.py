# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-17 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import src.posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170714_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='### ATENÇÃO - TAMANHO DA IMAGEM PRECISA SER 555x235 NOTICIA OU 265x360 PARA LAZER / TURISMO ###', null=True, upload_to=src.posts.models.upload_location),
        ),
    ]