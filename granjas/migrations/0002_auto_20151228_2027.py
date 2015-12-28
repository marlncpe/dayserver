# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('granjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='corrale',
            name='galpon',
            field=models.ForeignKey(default=datetime.datetime(2015, 12, 28, 20, 27, 43, 460620), to='granjas.Galpone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galpone',
            name='granja',
            field=models.ForeignKey(default=datetime.datetime(2015, 12, 28, 20, 27, 48, 219997), to='granjas.Granja'),
            preserve_default=False,
        ),
    ]
