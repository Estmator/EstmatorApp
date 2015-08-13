from __future__ import unicode_literals
from django.test import TestCase
from est_client.models import Client, Company
from estmator_project.factories import ClientFactory, CompanyFactory


class TestCompanyModel(TestCase):
    def setUp(self):
        self.company = CompanyFactory()

    def test_company_add(self):
        self.assertTrue(len(Company.objects.all()), 1)
        CompanyFactory()
        CompanyFactory()
        self.assertTrue(len(Company.objects.all()), 3)

    def test_company_delete(self):
        com1 = CompanyFactory()
        com2 = CompanyFactory()
        self.assertTrue(len(Company.objects.all()), 3)
        com1.delete()
        com2.delete()
        self.assertTrue(len(Company.objects.all()), 1)

    def test_company_str(self):
        name = self.company.company_name
        self.assertTrue(Company.objects.first(), name)

    def test_company_name(self):
        self.assertLess(len(self.company.company_name), 256)

    def test_company_phone(self):
        self.assertIsNotNone(self.company.phone)

    def test_company_address(self):
        pass

    def test_company_city(self):
        pass

    def test_company_state(self):
        pass

    def test_company_postal(self):
        pass

    def test_company_rates(self):
        pass

    def tearDown(self):
        Company.objects.all().delete()


class TestClientModel(TestCase):
    def setUp(self):
        self.client = ClientFactory()

    def test_client_add(self):
        self.assertTrue(len(Client.objects.all()), 1)
        ClientFactory()
        ClientFactory()
        self.assertTrue(len(Client.objects.all()), 3)

    def test_client_delete(self):
        cli1 = ClientFactory()
        cli2 = ClientFactory()
        self.assertTrue(len(Client.objects.all()), 3)
        cli1.delete()
        cli2.delete()
        self.assertTrue(len(Client.objects.all()), 1)

    def test_client_edit(self):
        pass

    def test_client_str(self):
        pass

    def test_company_client_relationship(self):
        pass

    def test_first_last_name(self):
        pass

    def test_title(self):
        pass

    def test_cell_desk_phone(self):
        pass

    def test_email(self):
        pass

    def tearDown(self):
        Client.objects.all().delete()
