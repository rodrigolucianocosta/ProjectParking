# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0004_auto_20150417_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='carro',
            field=models.ForeignKey(to='Parking.carro', null=True),
            preserve_default=True,
        ),
    ]
