# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0016_auto_20150418_0909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaga',
            old_name='Saida',
            new_name='saida',
        ),
        migrations.RenameField(
            model_name='vaga',
            old_name='ValorHora',
            new_name='valorHora',
        ),
        migrations.RemoveField(
            model_name='vaga',
            name='Entrada',
        ),
        migrations.AddField(
            model_name='vaga',
            name='entrada',
            field=models.DateTimeField(null=True, verbose_name=b'entrada'),
            preserve_default=True,
        ),
    ]
