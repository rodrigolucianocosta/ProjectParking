# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0010_auto_20150418_0632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaga',
            name='carro',
        ),
        migrations.RemoveField(
            model_name='vaga',
            name='id',
        ),
        migrations.AddField(
            model_name='vaga',
            name='tipoVaga',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Tipo de Vaga', choices=[(b'A', b'Carro'), (b'B', b'Moto'), (b'C', b'Caminhao')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vaga',
            name='numero',
            field=models.AutoField(serialize=False, verbose_name=b'numero da vaga', primary_key=True),
        ),
    ]
