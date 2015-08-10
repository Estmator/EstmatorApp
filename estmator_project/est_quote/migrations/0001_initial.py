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
                ('client', models.ForeignKey(related_name='client', to='est_client.Client')),
                ('products', models.ManyToManyField(related_name='products', through='est_quote.ProductInQuote', to='est_quote.Product', blank=True)),
                ('user', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='productinquote',
            name='quote',
            field=models.ForeignKey(blank=True, to='est_quote.Quote', null=True),
        ),
    ]
