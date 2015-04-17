# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0002_auto_20150417_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='marca',
            field=models.CharField(max_length=20, null=True, verbose_name=b'maraca\\modelo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carro',
            name='placa',
            field=models.CharField(max_length=10, null=True, verbose_name=b'placa'),
            preserve_default=True,
        ),
    ]
