# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0003_auto_20150417_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, verbose_name=b'nome')),
                ('cpf', models.IntegerField(max_length=11, verbose_name=b'cpf')),
                ('rg', models.CharField(max_length=20, verbose_name=b'rg')),
                ('telefone', models.IntegerField(max_length=9, verbose_name=b'telefone')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='carro',
            name='cor',
            field=models.CharField(max_length=10, null=True, verbose_name=b'cor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carro',
            name='marca',
            field=models.CharField(max_length=20, null=True, verbose_name=b'marca'),
        ),
        migrations.AlterField(
            model_name='carro',
            name='placa',
            field=models.CharField(max_length=10, null=True, verbose_name=b'placa do veiculo'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='numero',
            field=models.IntegerField(max_length=2, verbose_name=b'numero da vaga'),
        ),
    ]
