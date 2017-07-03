from django.shortcuts import resolve_url as r
from django.test import TestCase


def assertContents(self, contents):
    for expected_content in contents:
        with self.subTest():
            self.assertContains(self.response, expected_content)


class TicketsTest(TestCase):
    """

    """
    # def setUp(self):
    #     self.empresa = Empresa.objects.create(nome='Vivo', slug='vivo', logo='logo.png')
    #     self.response = self.client.get(r('core:home'))
    #
    # def test_get(self):
    #     self.assertEqual(200, self.response.status_code)
    #
    # def test_template(self):
    #     """Must use core/empresa_list.html"""
    #     self.assertTemplateUsed(self.response, 'core/empresa_list.html')

