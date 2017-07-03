from django.contrib.auth.models import User
from django.core import urlresolvers
from django.core.exceptions import ValidationError
from django.test import TestCase

from src.core.models import Empresa
from src.tickets.models import Ticket, TIPO_CHOICES, STATUS_CHOICES


def assertContents(self, contents):
    for expected_content in contents:
        with self.subTest():
            self.assertContains(self.response, expected_content)


class TicketModelManagerTest(TestCase):
    fixtures = ['empresas.json', 'users.json']

    def test_ticket_representante(self):
        empresa = Empresa.objects.first()
        user = User.objects.first()
        ticket = Ticket.objects.representante_empresa(empresa=empresa, user=user)
        self.assertTrue(Ticket.objects.exists())

    def test_ticket_cadastro_nova_empresa(self):
        user = User.objects.first()
        Ticket.objects.cadastro_empresa(nome='Tim', cidade='Ciudad del Este', endereco='Rua da Silva, 155', user=user)
        ticket = Ticket.objects.filter(tipo=TIPO_CHOICES[1][0]).first()
        self.assertEqual(1, ticket.tipo)


class TicketModelTest(TestCase):
    """Tickets """
    def setUp(self):
        self.user = User.objects.create_superuser(username='jacob', password='top_secret', email='tyow@hotmail.com.br')
        self.client.login(username=self.user.username, password='top_secret')
        self.ticket = Ticket.objects.create(criador=self.user, object_id=1)
        self.ticket2 = Ticket.objects.cadastro_empresa(
            nome='Partiu',
            cidade='Ciudad del Este',
            endereco='Rua da Silva, 155',
            user=self.user
        )

    def test_create(self):
        self.assertTrue(Ticket.objects.exists())

    def test_status_choices(self):
        """ Ticket status deve ser '0', '1', '2', '3'"""
        ticket = Ticket(status='X')
        self.assertRaises(ValidationError, ticket.full_clean)

