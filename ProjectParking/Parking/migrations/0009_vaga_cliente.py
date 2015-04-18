# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0008_auto_20150418_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='cliente',
            field=models.OneToOneField(null=True, verbose_name=b'cliente', to='Parking.cliente'),
            preserve_default=True,
        ),
    ]
