# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('est_quote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoteproperties',
            name='glob_vars',
        ),
        migrations.RemoveField(
            model_name='quoteproperties',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='global_mods',
        ),
        migrations.DeleteModel(
            name='QuoteProperties',
        ),
    ]
