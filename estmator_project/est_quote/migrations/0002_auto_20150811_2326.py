# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('est_quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='l_cart',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='m_cart',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='mins_piece',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='mult_dollies',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_cart',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='s_pack',
            field=models.FloatField(),
        ),
    ]
