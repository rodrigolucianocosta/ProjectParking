# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0023_auto_20150623_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='entrada',
            field=models.TimeField(null=True, verbose_name=b'entrada'),
        ),
    ]
