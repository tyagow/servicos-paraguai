# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-23 23:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20161212_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimento',
            name='descricao_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='estabelecimento',
            name='descricao_pt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='caracteristica',
            name='estabelecimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caracteristicas', to='core.Estabelecimento'),
        ),
        migrations.AlterField(
            model_name='preco',
            name='estabelecimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='precos', to='core.Estabelecimento'),
        ),
    ]
