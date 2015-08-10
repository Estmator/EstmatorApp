# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('est_quote', '0003_auto_20150810_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='user',
            field=models.ForeignKey(related_name='user_quotes', editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
