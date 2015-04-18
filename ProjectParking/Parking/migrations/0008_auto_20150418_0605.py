# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0007_auto_20150418_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='carro',
            field=models.ForeignKey(verbose_name=b'carro', to='Parking.carro'),
        ),
    ]
