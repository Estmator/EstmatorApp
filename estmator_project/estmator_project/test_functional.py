from django.contrib.staticfiles.testing import LiveServerTestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from splinter import Browser
from time import sleep

from .factories import (
    UserFactory, ClientFactory, CompanyFactory, CategoryFactory,
    ProductFactory, QuoteFactory, QuoteModsFactory)


class LiveServerSplinterAuthTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(LiveServerSplinterAuthTest, cls).setUpClass()
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

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(LiveServerSplinterAuthTest, cls).tearDownClass()
        sleep(3)

    def login_helper(self, username, password):
        self.browser.visit('{}{}'.format(
            self.live_server_url, '/accounts/login/')
        )

        self.browser.fill('username', username)
        self.browser.fill('password', password)
        self.browser.find_by_value('Log in').first.click()

    def setUp(self):
        self.login_helper(self.user1.username, 'secret')
        pass

    # def test_redirected_to_menu_after_login(self):
    #     self.login_helper(self.user1.username, 'secret')
    #     self.browser.visit('{}{}'.format(
    #         self.live_server_url, '/menu')
    #     )
    #     self.assertTrue(self.browser.is_text_present('Select An Option'))

    def test_new_quote_button(self):
        self.browser.visit('{}{}'.format(
            self.live_server_url, '/menu')
        )
        new_quote_visible = self.browser.find_by_id('new_quote').visible
        self.assertFalse(new_quote_visible)

        self.browser.find_by_id('btn_new_quote').click()
        self.assertTrue(self.browser.is_text_present('New Quote'))

        new_quote_visible = self.browser.find_by_id('new_quote').visible
        sleep(1)
        self.assertTrue(new_quote_visible)

