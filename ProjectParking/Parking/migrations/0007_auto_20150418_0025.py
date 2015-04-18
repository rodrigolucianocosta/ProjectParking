# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0006_auto_20150417_2354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carro',
            options={'verbose_name': 'carro', 'verbose_name_plural': 'carros'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'cliente', 'verbose_name_plural': 'clientes'},
        ),
        migrations.AlterModelOptions(
            name='vaga',
            options={'verbose_name': 'vaga', 'verbose_name_plural': 'vagas'},
        ),
        migrations.RemoveField(
            model_name='vaga',
            name='horarioEntrada',
        ),
        migrations.RemoveField(
            model_name='vaga',
            name='horarioSaida',
        ),
        migrations.AddField(
            model_name='vaga',
            name='Entrada',
            field=models.DateTimeField(null=True, verbose_name=b'Entrada'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vaga',
            name='Saida',
            field=models.DateTimeField(null=True, verbose_name=b'Saida'),
            preserve_default=True,
        ),
    ]
