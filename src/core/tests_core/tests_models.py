from django.test import TestCase
from django.shortcuts import resolve_url as r
from src.core.models import Estabelecimento, Categoria


class EstabelecimentoModelTest(TestCase):
    def setUp(self):
        self.obj = Estabelecimento.objects.create(
            nome='Fast Way',
            website='www.fastway.com',
            slug='fast-way',
            endereco='Avda. Rogelio Benitez, 061 500 763',
        )

    def test_create(self):
        self.assertTrue(Estabelecimento.objects.exists())

    def test_get_absolute_url(self):
        url = r('estabelecimento_detail', slug=self.obj.slug)
        self.assertEqual(url, self.obj.get_absolute_url())


class CategoryModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(
            nome='Alimentação',
            slug='alimentacao',
        )

    def test_create_category(self):

        self.assertTrue(Categoria.objects.exists())

    def test_get_absolute_url(self):
        url = r('categoria_detail', slug=self.categoria.slug)
        self.assertEqual(url, self.categoria.get_absolute_url())


