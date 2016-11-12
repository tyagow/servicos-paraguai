from django.test import TestCase
from core.models import Store, Category


class LojaModelTest(TestCase):
    def setUp(self):
        self.obj = Store.objects.create(
            name='Fast Way',
            website='www.fastway.com',
            phone='+595 61 500 763',
            slug='fast-way',
        )

    def test_create(self):
        self.assertTrue(Store.objects.exists())


class CategoryModelTest(TestCase):
    def test_create_category(self):
        Category.objects.create(
            name='Alimentação'
        )
        self.assertTrue(Category.objects.exists())
