from django.test import TestCase
from django.utils.translation import ugettext_lazy as _

from src.tickets.forms import TicketCreateForm


class TicketCreateFormTestCase(TestCase):
    def test_emtpy_form(self):
        form = TicketCreateForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'titulo': [_('Este campo é obrigatório.')],
            'descricao': [_('Este campo é obrigatório.')]
        })


