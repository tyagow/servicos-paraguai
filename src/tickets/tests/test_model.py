from django.contrib.auth.models import User
from django.core import urlresolvers
from django.core.exceptions import ValidationError
from django.test import TestCase

from src.tickets.models import Ticket, TIPO_CHOICES, STATUS_CHOICES


def assertContents(self, contents):
    for expected_content in contents:
        with self.subTest():
            self.assertContains(self.response, expected_content)


class TicketModelTest(TestCase):
    """Tickets """
    def setUp(self):
        self.user = User.objects.create_superuser(username='jacob', password='top_secret', email='tyow@hotmail.com.br')
        self.client.login(username=self.user.username, password='top_secret')
        self.ticket = Ticket.objects.create(criador=self.user, object_id=1)

    def test_create(self):
        self.assertTrue(Ticket.objects.exists())

    def test_status_choices(self):
        """ Ticket status deve ser '0', '1', '2', '3'"""
        ticket = Ticket(status='X')
        self.assertRaises(ValidationError, ticket.full_clean)

