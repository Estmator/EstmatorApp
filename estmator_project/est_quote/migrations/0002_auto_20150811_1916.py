# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('est_quote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductProperties',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(null=True, blank=True)),
                ('product', models.ForeignKey(blank=True, to='est_quote.Product', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('travel_time', models.IntegerField()),
                ('org_street_load', models.BooleanField()),
                ('org_midrise_elev_std', models.BooleanField()),
                ('org_midrise_elv_frt', models.BooleanField()),
                ('org_highrise', models.BooleanField()),
                ('org_stairs', models.BooleanField()),
                ('org_lng_psh', models.BooleanField()),
                ('dest_street_load', models.BooleanField()),
                ('dest_midrise_elev_std', models.BooleanField()),
                ('dest_midrise_elv_frt', models.BooleanField()),
                ('dest_highrise', models.BooleanField()),
                ('dest_stairs', models.BooleanField()),
                ('dest_lng_psh', models.BooleanField()),
                ('product', models.ForeignKey(blank=True, to='est_quote.Product', null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='GlobalVars',
            new_name='QuoteModifiers',
        ),
        migrations.RenameModel(
            old_name='GlobalMods',
            new_name='QuoteProperties',
        ),
        migrations.RemoveField(
            model_name='locvars',
            name='product',
        ),
        migrations.RemoveField(
            model_name='locvars',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='productinquote',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productinquote',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='loc_vars',
        ),
        migrations.AddField(
            model_name='quote',
            name='grand_total',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='global_mods',
            field=models.ManyToManyField(related_name='quote', through='est_quote.QuoteProperties', to='est_quote.GlobalVars', blank=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='products',
            field=models.ManyToManyField(related_name='quote', through='est_quote.ProductProperties', to='est_quote.Product', blank=True),
        ),
        migrations.DeleteModel(
            name='LocVars',
        ),
        migrations.DeleteModel(
            name='ProductInQuote',
        ),
        migrations.AddField(
            model_name='quoteoptions',
            name='quote',
            field=models.ForeignKey(blank=True, to='est_quote.Quote', null=True),
        ),
        migrations.AddField(
            model_name='productproperties',
            name='quote',
            field=models.ForeignKey(blank=True, to='est_quote.Quote', null=True),
        ),
    ]
