from django.test import TestCase

from core.models import Estabelecimento, Categoria


class EstabelecimentoModelTest(TestCase):
    def setUp(self):
        self.obj = Estabelecimento.objects.create(
            nome='Fast Way',
            website='www.fastway.com',
            slug='fast-way',
        )

    def test_create(self):
        self.assertTrue(Estabelecimento.objects.exists())


class CategoryModelTest(TestCase):
    def test_create_category(self):
        Categoria.objects.create(
            nome='Alimentação'
        )
        self.assertTrue(Categoria.objects.exists())


