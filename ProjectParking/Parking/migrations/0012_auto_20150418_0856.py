# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0011_auto_20150418_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='veiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fabricante', models.CharField(max_length=20, null=True, verbose_name=b'fabricante')),
                ('marca', models.CharField(max_length=20, null=True, verbose_name=b'marca')),
                ('cor', models.CharField(max_length=10, null=True, verbose_name=b'cor')),
                ('placa', models.CharField(max_length=10, null=True, verbose_name=b'placa do veiculo')),
            ],
            options={
                'verbose_name': 'veiculo',
                'verbose_name_plural': 'veiculos',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='carro',
        ),
        migrations.DeleteModel(
            name='carro',
        ),
        migrations.AddField(
            model_name='cliente',
            name='veiculo',
            field=models.ForeignKey(verbose_name=b'carro', to='Parking.veiculo', null=True),
            preserve_default=True,
        ),
    ]
