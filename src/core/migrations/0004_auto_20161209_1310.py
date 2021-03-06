# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_anuncio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('valor', models.CharField(max_length=250)),
                ('tipo', models.CharField(choices=[('D', 'Descrição'), ('P', 'Preço')], max_length=1)),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estabelecimento')),
            ],
        ),
        migrations.AlterField(
            model_name='categoria',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='categorias'),
        ),
    ]
