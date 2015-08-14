from django.contrib.staticfiles.testing import LiveServerTestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from splinter import Browser
from time import sleep

from .factories import (
    UserFactory, ClientFactory, CompanyFactory, CategoryFactory,
    ProductFactory, QuoteFactory, QuoteModsFactory)


class LiveServerSplinterTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(LiveServerSplinterTest, cls).setUpClass()
        cls.browser = Browser()
        cls.user1 = UserFactory()
        cls.user1.set_password('secret')
        cls.user1.save()

        cls.client1 = ClientFactory()

        cls.category1 = CategoryFactory(name='Chairs')
        cls.category2 = CategoryFactory(name='Tables')

        cls.product1 = ProductFactory(category=cls.category1)
        cls.product2 = ProductFactory(category=cls.category1)
        cls.product3 = ProductFactory(category=cls.category2)

        cls.login_helper(cls.user1.username, 'secret')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(LiveServerSplinterTest, cls).tearDownClass()
        sleep(3)

    @classmethod
    def login_helper(cls, username, password):
        cls.browser.visit('{}{}'.format(
            cls.live_server_url, '/accounts/login/')
        )

        cls.browser.fill('username', username)
        cls.browser.fill('password', password)
        cls.browser.find_by_value('Log in').first.click()

    def setUp(self):
        pass

    def test_auth_redirect_to_menu_page(self):
        self.browser.visit('{}{}'.format(
            self.live_server_url, '/menu')
        )

