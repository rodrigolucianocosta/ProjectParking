# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0019_veiculo_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaga',
            name='tipoVaga',
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='cliente',
            field=models.ForeignKey(verbose_name=b'cliente', to='Parking.cliente', null=True),
        ),
    ]
