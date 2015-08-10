# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('est_quote', '0002_auto_20150809_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='category',
            field=models.ManyToManyField(related_name='category', to='est_quote.Category'),
        ),
        migrations.AddField(
            model_name='quote',
            name='products',
            field=models.ManyToManyField(related_name='products', to='est_quote.Product'),
        ),
    ]
