from __future__ import unicode_literals
from django.test import TestCase
from est_quote.models import Category, Product, Quote, QuoteModifiers
from estmator_project.factories import (
    UserFactory, ClientFactory, CompanyFactory, CategoryFactory,
    ProductFactory, QuoteFactory, QuoteModsFactory)


class TestCategoryModel(TestCase):
    def setUp(self):
        pass

    def test_category_add(self):
        pass

    def test_category_delete(self):
        pass

    def test_category_edit(self):
        pass

    def test_category_invalid_chars_in_name(self):
        pass

    def tearDown(self):
        Category.objects.all().delete()


class TestProductModel(TestCase):
    def setUp(self):
        pass

    def test_product_add(self):
        pass

    def test_product_delete(self):
        pass

    def test_product_edit(self):
        pass

    def test_product_invalid_chars(self):
        pass

    def tearDown(self):
        Product.objects.all().delete()


class TestQuoteModel(TestCase):
    def setUp(self):
        quote_mods = QuoteModsFactory.create()

    def test_quote_add(self):
        pass

    def test_quote_delete(self):
        pass

    def test_quote_edit(self):
        pass

    def test_quote_invalid_chars(self):
        pass

    def tearDown(self):
        Quote.objects.all().delete()
        QuoteModifiers.objects.all().delete()
