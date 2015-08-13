from __future__ import unicode_literals
from django.test import TestCase
from est_quote.models import Category, Product, Quote
from estmator_project.factories import (
    CategoryFactory, ProductFactory, QuoteFactory)


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
