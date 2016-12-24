from django.shortcuts import resolve_url as r
from django.test import TestCase
from django.urls import reverse

from src.core.models import Estabelecimento, Categoria, Telefone, Preco


class HomeTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Alimentação', slug='alimentacao')
        Categoria.objects.create(nome='Bares', slug='bares', parent=self.categoria)

        self.estabelecimento = Estabelecimento.objects.create(
            nome='Fast Way',
            website='www.fastway.com',
            slug='fast-way',
            descricao='Fast Way Descrição',
            endereco='Avda. Rogelio Benitez, 061 500 763',
            cidade='S',
        )
        self.estabelecimento.categoria.add(self.categoria)
        self.response = self.client.get(r('home'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_input_search(self):
        self.assertContains(self.response, '<input')

    def test_html_categorias(self):
        """Html must display categories"""
        self.assertContains(self.response, self.categoria.nome)

    # def test_html_categorias_link(self):
    #     expected = 'href="{}"'.format(self.categoria.get_absolute_url())
    #     self.assertContains(self.response, expected)


class CategoriaDetailGet(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(
            nome='Alimentação',
            slug='alimentacao',
        )
        e1 = Estabelecimento.objects.create(
            nome='Fast Way',
            website='www.fastway.com',
            slug='fast-way',
            descricao='Fast Way Descrição',
            endereco='Avda. Rogelio Benitez, 061 500 763',
            cidade='S',
        )
        e1.categoria.add(self.categoria)
        self.response = self.client.get(r('categoria_detail', slug='alimentacao'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/categoria_detail.html')

    def test_html(self):
        contents = [
            'Fast Way',
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)


class EstabelecimentoDetailGet(TestCase):
    def setUp(self):
        e1 = Estabelecimento.objects.create(
            nome='Fast Way',
            website='www.fastway.com',
            slug='fast-way',
            descricao='Fast Way Descrição',
            endereco='Avda. Rogelio Benitez, 061 500 763',
            cidade='S',
        )
        Telefone.objects.create(estabelecimento=e1, numero='123456')
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
            'Avda. Rogelio Benitez, 061 500 763',
            'Salto del Guairá',
            '123456',
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)


class HotelDetailGet(TestCase):
    def setUp(self):

        self.categoria = Categoria.objects.create(
            nome='Hospedagem',
            slug='Hospedagem',
        )
        e1 = Estabelecimento.objects.create(
            nome='Fast Way',
            website='www.hotel.com',
            slug='fast-way',
            descricao='Fast Way Descrição',
            endereco='Avda. Rogelio Benitez, 061 500 763',
            cidade='S',
        )
        e1.categoria.add(self.categoria)
        Telefone.objects.create(estabelecimento=e1, numero='123456')
        Preco.objects.create(estabelecimento=e1, titulo='Diária', valor='100.00')
        self.response = self.client.get(r('estabelecimento_detail', slug='fast-way'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/hotel_detail.html')

    def test_html(self):
        contents = [
            'Fast Way',
            'www.hotel.com',
            'Fast Way Descrição',
            'Avda. Rogelio Benitez, 061 500 763',
            'Salto del Guairá',
            '123456',
            'Diária',
            '100,00',
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)


class CategoriasGet(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Alimentação', slug='alimentacao')
        Categoria.objects.create(nome='Bares', slug='bares', parent=self.categoria)
        self.response = self.client.get(r('categorias'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_html_categorias(self):
        """Html must display categories"""
        self.assertContains(self.response, self.categoria.nome)

    def test_html_categorias_link(self):
        expected = 'href="{}"'.format(self.categoria.get_absolute_url())
        self.assertContains(self.response, expected)