from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from est_client.models import Client


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return 'Category: {}'.format(self.name)


@python_2_unicode_compatible
class Product(models.Model):
    # Inputs
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=256)

    # Piece Multipliers
    mins_piece = models.IntegerField()
    mult_dollies = models.IntegerField()
    m_cart = models.IntegerField()
    l_cart = models.IntegerField()
    p_cart = models.IntegerField()
    s_pack = models.IntegerField()

    def __str__(self):
        return 'Product: {}'.format(self.name)


class ProductInQuote(models.Model):
    quote = models.ForeignKey('Quote', null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True)
    counts = models.IntegerField(blank=True, null=True)

    # Outputs
    @property
    def total_mins(self):
        return self.counts * self.mins_piece

    @property
    def dollies(self):
        return self.counts * self.mult_dollies

    @property
    def machine_carts(self):
        return self.counts * self.m_cart

    @property
    def library_carts(self):
        return self.counts * self.l_cart

    @property
    def panel_carts(self):
        return self.counts * self.p_cart

    @property
    def speed_packs(self):
        return self.counts * self.s_pack


@python_2_unicode_compatible
class Quote(models.Model):
    user = models.ForeignKey(User, related_name='user')
    client = models.ForeignKey(Client, related_name='client')
    name = models.CharField(max_length=256)
    date = models.DateField(auto_now_add=True)
    products = models.ManyToManyField(
        Product,
        related_name='products',
        through=ProductInQuote,
        blank=True
    )

    def __str__(self):
        return 'Quote: {}'.format(self.name)
