from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from src.comments.models import Comment
from src.core.models import Estabelecimento


class CommentsModelTest(TestCase):
    def setUp(self):
        self.estabelecimento = Estabelecimento.objects.create(
            nome='Fast Way',
            website='www.fastway.com',
            slug='fast-way',
            endereco='Avda. Rogelio Benitez, 061 500 763',
        )
        content_type = ContentType.objects.get_for_model(self.estabelecimento.__class__)
        object_id = self.estabelecimento.id
        self.obj = Comment.objects.create(
            nome='Fast Way',
            conteudo='Conteudo',
            content_type=content_type,
            object_id=object_id,
        )

    def test_create(self):
        self.assertTrue(Comment.objects.exists())

    def test_str(self):
        self.assertEqual(str(self.obj), self.obj.nome)

    def test_aprovado_default_false(self):
        self.assertTrue(not self.obj.aprovado)

    def test_filter_by_instance(self):
        self.obj.aprovado = True
        self.obj.save()
        comments = Comment.objects.filter_by_instance(self.estabelecimento)
        self.assertEqual(comments[0], self.obj)