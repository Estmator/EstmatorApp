# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('est_quote', '0002_auto_20150810_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalVars',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_load', models.FloatField()),
                ('midrise_elev_std', models.FloatField()),
                ('midrise_elv_frt', models.FloatField()),
                ('highrise', models.FloatField()),
                ('stairs', models.FloatField()),
                ('lng_psh', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='globalmods',
            name='highrise',
        ),
        migrations.RemoveField(
            model_name='globalmods',
            name='lng_psh',
        ),
        migrations.RemoveField(
            model_name='globalmods',
            name='midrise_elev_std',
        ),
        migrations.RemoveField(
            model_name='globalmods',
            name='midrise_elv_frt',
        ),
        migrations.RemoveField(
            model_name='globalmods',
            name='product',
        ),
        migrations.RemoveField(
            model_name='globalmods',
            name='stairs',
        ),
        migrations.RemoveField(
            model_name='globalmods',
            name='street_load',
        ),
        migrations.AlterField(
            model_name='quote',
            name='global_mods',
            field=models.ManyToManyField(related_name='globals', through='est_quote.GlobalMods', to='est_quote.GlobalVars', blank=True),
        ),
        migrations.AddField(
            model_name='globalmods',
            name='glob_vars',
            field=models.ForeignKey(blank=True, to='est_quote.GlobalVars', null=True),
        ),
    ]
