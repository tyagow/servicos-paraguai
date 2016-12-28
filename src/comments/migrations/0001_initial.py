# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-26 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('object_id', models.PositiveIntegerField()),
                ('conteudo', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('aprovado', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]