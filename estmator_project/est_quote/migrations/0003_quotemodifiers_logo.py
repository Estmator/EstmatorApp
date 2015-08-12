# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('est_quote', '0002_auto_20150811_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotemodifiers',
            name='logo',
            field=models.ImageField(default=None, upload_to='photo_files/%Y-%m-%d'),
            preserve_default=False,
        ),
    ]
