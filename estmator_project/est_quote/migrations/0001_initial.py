# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('est_client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalMods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
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
        migrations.CreateModel(
            name='LocVars',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('mins_piece', models.IntegerField()),
                ('mult_dollies', models.IntegerField()),
                ('m_cart', models.IntegerField()),
                ('l_cart', models.IntegerField()),
                ('p_cart', models.IntegerField()),
                ('s_pack', models.IntegerField()),
                ('category', models.ForeignKey(to='est_quote.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInQuote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('counts', models.IntegerField(null=True, blank=True)),
                ('product', models.ForeignKey(blank=True, to='est_quote.Product', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('date', models.DateField(auto_now_add=True)),
                ('sub_total', models.IntegerField(null=True, blank=True)),
                ('client', models.ForeignKey(related_name='client', to='est_client.Client')),
                ('global_mods', models.ManyToManyField(related_name='globals', through='est_quote.GlobalMods', to='est_quote.GlobalVars', blank=True)),
                ('loc_vars', models.ManyToManyField(related_name='loc_vars', through='est_quote.LocVars', to='est_quote.Product', blank=True)),
                ('products', models.ManyToManyField(related_name='products', through='est_quote.ProductInQuote', to='est_quote.Product', blank=True)),
                ('user', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='productinquote',
            name='quote',
            field=models.ForeignKey(blank=True, to='est_quote.Quote', null=True),
        ),
        migrations.AddField(
            model_name='locvars',
            name='product',
            field=models.ForeignKey(blank=True, to='est_quote.Product', null=True),
        ),
        migrations.AddField(
            model_name='locvars',
            name='quote',
            field=models.ForeignKey(blank=True, to='est_quote.Quote', null=True),
        ),
        migrations.AddField(
            model_name='globalmods',
            name='glob_vars',
            field=models.ForeignKey(blank=True, to='est_quote.GlobalVars', null=True),
        ),
        migrations.AddField(
            model_name='globalmods',
            name='quote',
            field=models.ForeignKey(blank=True, to='est_quote.Quote', null=True),
        ),
    ]
