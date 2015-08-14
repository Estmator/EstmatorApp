from django.test import TestCase, Client


class TestConnectionView(TestCase):

    def setUp(self):
        self.c = Client()

    def test_get_204(self):
        self.res = self.c.get('/connection-test')
        self.assertEqual(self.res.status_code, 204)
