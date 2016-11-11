from django.test import TestCase
from core.models import Client


class ClientModelTest(TestCase):
    def test_create(self):
        Client.objects.create(
            name='Fast Way',
            website='www.fastway.com',
            phone='+595 61 500 763'
        )
        self.assertTrue(Client.objects.exists())