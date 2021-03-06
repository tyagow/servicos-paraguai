# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 22:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('slug', models.SlugField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='core.Categoria')),
            ],
            options={
                'verbose_name_plural': 'Categorias',
                'verbose_name': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('website', models.URLField()),
                ('slug', models.SlugField(unique=True)),
                ('logo', models.ImageField(null=True, upload_to='')),
                ('descricao', models.TextField()),
                ('endereco', models.CharField(max_length=60)),
                ('cidade', models.CharField(choices=[('E', 'Ciudad del Este'), ('P', 'Pedro Juan Caballero'), ('S', 'Salto del Guairá')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('coordenadas', models.CharField(blank=True, max_length=40, null=True, verbose_name='Coordenadas')),
                ('categoria', models.ManyToManyField(blank=True, related_name='estabelecimentos', to='core.Categoria')),
            ],
            options={
                'verbose_name_plural': 'Estabelecimentos',
                'ordering': ['nome'],
                'verbose_name': 'Estabelecimento',
            },
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estabelecimento')),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(blank=True, max_length=15, null=True)),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefones', to='core.Estabelecimento')),
            ],
        ),
    ]
