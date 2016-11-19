from django.shortcuts import resolve_url as r
from django.test import TestCase

from core.models import Estabelecimento


class HomeTest(TestCase):
    def test_get(self):
        response = self.client.get(r('home'))
        self.assertEqual(200, response.status_code)


class EstabelecimentoDetailGet(TestCase):
    def setUp(self):
        Estabelecimento.objects.create(
            nome='Fast Way',
            website='www.fastway.com',
            slug='fast-way',
            descricao='Fast Way Descrição',
            endereco='Fast Way Endereço',
            cidade='S',
        )
        self.response = self.client.get(r('estabelecimento_detail', slug='fast-way'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/estabelecimento_detail.html')

    def test_html(self):
        contents = [
            'Fast Way',
            'www.fastway.com',
            'Fast Way Descrição',
            'Fast Way Endereço',
            'Salto del Guairá',

        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)