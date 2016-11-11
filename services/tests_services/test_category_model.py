from django.test import TestCase
from services.models import Category


class CategoryModelTest(TestCase):
    def test_create_category(self):
        Category.objects.create(
            name='Alimentação'
        )
        self.assertTrue(True)
