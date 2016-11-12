from django.shortcuts import resolve_url as r
from django.test import TestCase


class HomeTest(TestCase):
    def test_get(self):
        response = self.client.get(r('home'))
        self.assertEqual(200, response.status_code)