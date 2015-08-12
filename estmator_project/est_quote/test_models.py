from __future__ import unicode_literals
from django.test import TestCase
from est_quote.models import Category, Product, Quote, QuoteModifiers
from estmator_project.factories import (
    UserFactory, ClientFactory, CompanyFactory, CategoryFactory,
    ProductFactory, QuoteFactory, QuoteModsFactory)


class TestCategoryModel(TestCase):
    def setUp(self):
        cat = CategoryFactory()
        cat.save()

    def test_category_add(self):
        self.assertTrue(len(Category.objects.all()), 1)
        cat1 = CategoryFactory()
        cat1.save()
        cat2 = CategoryFactory()
        cat2.save()
        self.assertTrue(len(Category.objects.all()), 3)

    def test_category_delete(self):
        self.assertTrue(len(Category.objects.all()), 1)
        cat1 = CategoryFactory()
        cat1.save()
        self.assertTrue(len(Category.objects.all()), 2)
        cat1.delete()
        self.assertTrue(len(Category.objects.all()), 1)

    def test_category_edit(self):
        cat1 = CategoryFactory()
        cat1.save()
        org_name = cat1.name
        cat1.name = 'Monkeys'
        self.assertNotEqual(org_name, cat1.name)

    def tearDown(self):
        Category.objects.all().delete()


class TestProductModel(TestCase):
    def setUp(self):
        cat = CategoryFactory()
        self.prod = ProductFactory(category=cat)
        self.prod2 = ProductFactory(category=cat)

    def test_product_category_change(self):
        self.assertTrue(self.prod.category, self.prod2.category)
        self.cat2 = CategoryFactory()
        self.prod.category = self.cat2
        self.assertTrue(self.prod.category, self.cat2)

    def test_product_add(self):
        self.assertTrue(len(Product.objects.all()), 2)
        ProductFactory()
        ProductFactory()
        self.assertTrue(len(Product.objects.all()), 4)

    def test_product_delete(self):
        self.assertTrue(len(Product.objects.all()), 2)
        prod3 = ProductFactory()
        prod4 = ProductFactory()
        self.assertTrue(len(Product.objects.all()), 4)
        prod3.delete()
        prod4.delete()
        self.assertTrue(len(Product.objects.all()), 2)

    def test_product_invalid_chars(self):
        pass

    def tearDown(self):
        Product.objects.all().delete()


# class TestQuoteModel(TestCase):
#     def setUp(self):
#         quote_mods = QuoteModsFactory.create()
#         quote_mods.save()

#     def test_quote_add(self):
#         pass

#     def test_quote_delete(self):
#         pass

#     def tearDown(self):
#         Quote.objects.all().delete()
#         QuoteModifiers.objects.all().delete()
