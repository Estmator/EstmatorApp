from django.contrib.staticfiles.testing import LiveServerTestCase

from splinter import Browser
from time import sleep

from .factories import (
    UserFactory, ClientFactory, CompanyFactory, CategoryFactory,
    ProductFactory, QuoteFactory, QuoteModsFactory)


class LiveServerSplinterAuthTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(LiveServerSplinterAuthTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LiveServerSplinterAuthTest, cls).tearDownClass()

    def setUp(self):
        self.user1 = UserFactory()
        self.user1.set_password('secret')
        self.user1.save()

        self.client1 = ClientFactory()

        self.category1 = CategoryFactory(name='Chairs')
        self.category2 = CategoryFactory(name='Tables')

        self.product1 = ProductFactory(category=self.category1)
        self.product2 = ProductFactory(category=self.category1)
        self.product3 = ProductFactory(category=self.category2)

        self.browser = Browser()
        self.login_helper(self.user1.username, 'secret')

    def tearDown(self):
        self.browser.quit()

    def login_helper(self, username, password):
        self.browser.visit('{}{}'.format(
            self.live_server_url, '/accounts/login/')
        )

        self.browser.fill('username', username)
        self.browser.fill('password', password)
        self.browser.find_by_value('Log in').first.click()

    def test_redirected_to_menu_after_login(self):
        self.assertTrue(self.browser.is_text_present('Select An Option'))

    def test_new_quote_button(self):
        self.browser.visit('{}{}'.format(
            self.live_server_url, '/menu')
        )
        new_quote_visible = self.browser.find_by_id('new_quote').visible
        self.assertFalse(new_quote_visible)

        self.browser.find_by_id('btn_new_quote').click()
        self.assertTrue(self.browser.is_text_present('New Quote'))
        sleep(1)
        new_quote_visible = self.browser.find_by_id('new_quote').visible
        self.assertTrue(new_quote_visible)

