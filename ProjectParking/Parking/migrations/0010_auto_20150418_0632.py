# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0009_vaga_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='ValorHora',
            field=models.FloatField(null=True, verbose_name=b'valorHora', validators=[django.core.validators.MinValueValidator(2.0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vaga',
            name='carro',
            field=models.OneToOneField(null=True, verbose_name=b'carro', to='Parking.carro'),
            preserve_default=True,
        ),
    ]
