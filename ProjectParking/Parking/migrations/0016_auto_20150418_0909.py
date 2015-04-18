# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0015_auto_20150418_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='veiculo',
            field=models.ForeignKey(verbose_name=b'veiculo', to='Parking.veiculo', null=True),
        ),
    ]
