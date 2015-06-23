# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0021_auto_20150623_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.IntegerField(verbose_name=b'telefone'),
        ),
    ]
