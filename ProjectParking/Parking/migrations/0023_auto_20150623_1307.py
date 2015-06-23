# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0022_auto_20150623_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='cliente',
            field=models.ForeignKey(verbose_name=b'cliente', to='Parking.cliente', null=True),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='entrada',
            field=models.TimeField(auto_now=True, verbose_name=b'entrada', null=True),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='saida',
            field=models.TimeField(null=True, verbose_name=b'Saida'),
        ),
    ]
