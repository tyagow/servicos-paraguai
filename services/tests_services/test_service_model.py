from django.test import TestCase

from core.models import Client
from services.models import Service

from _datetime import datetime, timedelta


class ServiceModelTest(TestCase):
    def setUp(self):
        c = Client.objects.create(
            name='Fast Way',
            phone='+595 61 500 763',
            website='http://www.fastway.com.py/',
        )
        self.obj = Service.objects.create(
            client=c,
            address='Avda. Rogelio Benitez esq Aka Karaya - Barrio Boqueron',
            city='Ciudad del Este',
            logo='logo1.png',
        )

    def test_create(self):
        self.assertTrue(Service.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_paid_default_to_false(self):
        """By default paid must be False"""
        self.assertEqual(False, self.obj.paid)
