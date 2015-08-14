# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import est_quote.models


class Migration(migrations.Migration):

    dependencies = [
        ('est_quote', '0005_quote_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='token',
            field=models.CharField(default=est_quote.models.make_token, max_length=36, editable=False),
        ),
    ]
