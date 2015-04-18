# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0013_cliente_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='tipoVaga',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Tipo de Vaga', choices=[(b'A', b'Carro'), (b'B', b'Moto'), (b'C', b'Caminhao')]),
            preserve_default=True,
        ),
    ]
