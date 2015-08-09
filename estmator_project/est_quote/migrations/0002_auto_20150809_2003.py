# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('est_quote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='company',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='contact',
        ),
        migrations.AlterField(
            model_name='quote',
            name='user',
            field=models.ForeignKey(related_name='user_quotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
