# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('address2', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='company',
            field=models.ForeignKey(to='est_client.Company'),
        ),
    ]
