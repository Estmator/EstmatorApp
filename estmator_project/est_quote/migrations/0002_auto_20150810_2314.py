# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('est_quote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalMods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_load', models.FloatField()),
                ('midrise_elev_std', models.FloatField()),
                ('midrise_elv_frt', models.FloatField()),
                ('highrise', models.FloatField()),
                ('stairs', models.FloatField()),
                ('lng_psh', models.FloatField()),
                ('product', models.ForeignKey(blank=True, to='est_quote.Product', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocVars',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('org_street_load', models.CharField(default='No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('org_midrise_elev_std', models.CharField(default='No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('org_midrise_elv_frt', models.CharField(default='No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('org_highrise', models.CharField(default='No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('org_stairs', models.CharField(default='No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('org_lng_psh', models.CharField(default='No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('dest_street_load', models.CharField(default='No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('dest_midrise_elev_std', models.CharField(default='No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('dest_midrise_elv_frt', models.CharField(default='No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('dest_highrise', models.CharField(default='No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('dest_stairs', models.CharField(default='No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('dest_lng_psh', models.CharField(default='No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])),
                ('product', models.ForeignKey(blank=True, to='est_quote.Product', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='sub_total',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='locvars',
            name='quote',
            field=models.ForeignKey(blank=True, to='est_quote.Quote', null=True),
        ),
        migrations.AddField(
            model_name='globalmods',
            name='quote',
            field=models.ForeignKey(blank=True, to='est_quote.Quote', null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='global_mods',
            field=models.ManyToManyField(related_name='globals', through='est_quote.GlobalMods', to='est_quote.Product', blank=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='loc_vars',
            field=models.ManyToManyField(related_name='loc_vars', through='est_quote.LocVars', to='est_quote.Product', blank=True),
        ),
    ]
