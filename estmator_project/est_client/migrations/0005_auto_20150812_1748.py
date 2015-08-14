# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('est_client', '0004_auto_20150812_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='ot_rate',
            field=models.IntegerField(default=40),
        ),
        migrations.AlterField(
            model_name='company',
            name='st_rate',
            field=models.IntegerField(default=30),
        ),
    ]
