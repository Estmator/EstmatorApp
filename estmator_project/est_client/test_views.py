from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from . import models
from estmator_project.factories import (
    UserFactory, ClientFactory, CompanyFactory, CategoryFactory,
    ProductFactory, QuoteFactory, QuoteModsFactory
)


class TestAPIClientView(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.c = Client()

    def test_denied_if_no_login(self):
        self.res = self.c.post('/api/v1/client/', follow=True)
        self.assertEqual(self.res.status_code, 200)
        self.assertIn('Log in', self.res.content)

    def test_client_added(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )
        client = ClientFactory()
        self.res = self.c.post('/api/v1/client/', {
            'company': client.company.id,
            'first_name': client.first_name,
            'last_name': client.last_name,
            'title': client.title,
            'cell': client.cell,
            'desk': client.desk,
            'email': client.email
        })
        self.assertEqual(models.Client.objects.count(), 2)

    def test_client_edited(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )
        client = ClientFactory()
        self.res = self.c.post('/api/v1/client/', {
            'client': client.id,
            'company': client.company.id,
            'first_name': client.first_name,
            'last_name': client.last_name,
            'title': client.title,
            'cell': client.cell,
            'desk': client.desk,
            'email': 'newemail'
        })
        self.assertEqual(models.Client.objects.count(), 1)
        self.assertEqual(models.Client.objects.get(id=client.id).email, 'newemail')
