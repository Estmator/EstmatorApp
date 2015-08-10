# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('est_quote', '0005_auto_20150810_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='date',
            field=models.DateField(default='2015-08-10', auto_now_add=True),
            preserve_default=False,
        ),
    ]
