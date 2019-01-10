# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('est_client', '0002_auto_20150812_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
