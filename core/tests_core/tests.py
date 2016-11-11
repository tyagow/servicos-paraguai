from django.test import TestCase
from core.models import Loja, Category


class LojaModelTest(TestCase):
    def test_create(self):
        Loja.objects.create(
            name='Fast Way',
            website='www.fastway.com',
            phone='+595 61 500 763'
        )
        self.assertTrue(Loja.objects.exists())


class CategoryModelTest(TestCase):
    def test_create_category(self):
        Category.objects.create(
            name='Alimentação'
        )
        self.assertTrue(Category.objects.exists())
