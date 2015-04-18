# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0005_cliente_carro'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='horarioEntrada',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vaga',
            name='horarioSaida',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='carro',
            field=models.ForeignKey(to='Parking.carro'),
        ),
    ]
