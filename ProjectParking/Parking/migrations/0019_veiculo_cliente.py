# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0018_remove_cliente_veiculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='cliente',
            field=models.ForeignKey(verbose_name=b'veiculo', to='Parking.cliente', null=True),
            preserve_default=True,
        ),
    ]
