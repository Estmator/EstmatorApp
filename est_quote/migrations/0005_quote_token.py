# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('est_quote', '0004_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='token',
            field=models.CharField(default=b'ff4543c0-2038-41d4-90a8-59f654abedc5', max_length=36),
        ),
    ]
