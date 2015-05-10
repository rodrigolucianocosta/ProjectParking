# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0017_auto_20150418_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='veiculo',
        ),
    ]
