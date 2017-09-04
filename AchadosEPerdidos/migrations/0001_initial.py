# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='objeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeObjeto', models.CharField(max_length=100)),
                ('localEncontrado', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('categoria', models.CharField(max_length=100, null=True)),
                ('faculdade', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=500, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('retirado', models.CharField(max_length=1)),
                ('nomePessoaRetirado', models.CharField(max_length=100, null=True)),
                ('identidade', models.CharField(max_length=20, null=True)),
                ('telefoneContato', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]