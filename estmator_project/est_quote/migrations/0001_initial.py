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
            name='ProductProperties',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(null=True, blank=True)),
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
                ('grand_total', models.IntegerField(null=True, blank=True)),
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
                ('client', models.ForeignKey(related_name='client', to='est_client.Client')),
                ('products', models.ManyToManyField(related_name='quote', through='est_quote.ProductProperties', to='est_quote.Product', blank=True)),
                ('user', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteModifiers',
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
        migrations.AddField(
            model_name='productproperties',
            name='quote',
            field=models.ForeignKey(blank=True, to='est_quote.Quote', null=True),
        ),
    ]
