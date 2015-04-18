# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0014_veiculo_tipovaga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='tipoVaga',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='tipoVeiculo',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Tipo de veiculo', choices=[(b'A', b'carro'), (b'B', b'moto'), (b'C', b'Caminhao')]),
            preserve_default=True,
        ),
    ]
