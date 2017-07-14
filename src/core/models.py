# -*- coding: utf-8 -*-
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.shortcuts import resolve_url as r
from imagekit.models import ImageSpecField
from mptt.fields import TreeManyToManyField
from mptt.models import MPTTModel, TreeForeignKey
from pilkit.processors import ResizeToFit
from star_ratings.models import Rating

from src.comments.models import Comment
from src.core.managers import  AnuncioManager, EstabelecimentoManager
from src.core.utils import path_and_rename_logo, path_and_rename_fotos, path_and_rename_categoria, \
    path_and_rename_banner
from django.utils.translation import ugettext as _


class Estabelecimento(models.Model):

    CIDADES = (
        ('E', 'Ciudad del Este'),
        ('P', 'Pedro Juan Caballero'),
        ('S', 'Salto del Guairá'),

    )
    nome = models.CharField(max_length=120)
    recomendado = models.BooleanField(default=False, blank=True)
    website = models.URLField()
    slug = models.SlugField(unique=True)
    logo = models.ImageField(upload_to=path_and_rename_logo, null=True)
    descricao = models.TextField()
    endereco = models.CharField(max_length=60)
    cidade = models.CharField(max_length=1, choices=CIDADES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    coordenadas = models.CharField('Coordenadas', null=True, blank=True, max_length=40)
    categoria = TreeManyToManyField('Categoria', blank=True, related_name='estabelecimentos')

    nota = GenericRelation(Rating, related_query_name='estabelecimentos')


    objects = EstabelecimentoManager()

    class Meta:
        verbose_name = 'Estabelecimento'
        verbose_name_plural = 'Estabelecimentos'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_coordenadas(self):
        if self.coordenadas:
            return self.coordenadas
        else:
            return "-25.513475,-54.615440"

    def get_latitude_longitde(self):
        return map(lambda x: float(x), self.coordenadas.split(','))

    def serializer(obj):
        latitude, longitude = obj.get_latitude_longitde()
        return dict(nome=obj.nome, latitude=latitude, longitude=longitude, categoria_icon=obj.get_categoria_icon())

    def get_absolute_url(self):
        return r('estabelecimento_detail', slug=self.slug)

    def get_categoria_icon(self):
        categoria_principal = None
        for categoria in self.categoria.all():
            if not categoria.parent == None:
                categoria_principal = categoria.parent
            else:
                categoria_principal = categoria
                break
        return categoria_principal.logo_thumbnail.url

    @property
    def is_hotel(self):
        return len(self.categoria.filter(nome__icontains=_('Hospedagem'))) > 0

    @property
    def comments(self):
        qs = Comment.objects.filter_by_instance(self)
        return qs

    @property
    def get_content_type(self):
        return ContentType.objects.get_for_model(self.__class__)

    @staticmethod
    def get_cidade_index(cidade):
        if not cidade or 'todas' in cidade:
            return 'todas'
        for index, _cidade in Estabelecimento.CIDADES:
            if cidade in _cidade:
                return index
        return None


class Telefone(models.Model):
    estabelecimento = models.ForeignKey('Estabelecimento', related_name='telefones')
    numero = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.numero


class Foto(models.Model):
    estabelecimento = models.ForeignKey('Estabelecimento')
    foto = models.ImageField(upload_to=path_and_rename_fotos, null=True, blank=True)

    def __str__(self):
        return self.foto.name


class Categoria(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    nome = models.CharField(max_length=60)
    slug = models.SlugField()
    logo = models.ImageField(upload_to=path_and_rename_categoria, null=True, blank=True)
    logo_thumbnail = ImageSpecField(source='logo',
                                      processors=[ResizeToFit(32, 32)],
                                      format='PNG',
                                      options={'quality': 100})

    class MPTTMeta:
        order_insertion_by = ['nome']

    def __str__(self):
        return self.nome

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    def get_absolute_url(self):
        return r('categoria_detail', slug=self.slug)


class Anuncio(models.Model):
    banner = models.ImageField(upload_to=path_and_rename_banner)
    url = models.URLField()
    estabelecimento = models.ForeignKey('Estabelecimento', blank=True, null=True)
    ativo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = AnuncioManager()

    def __str__(self):
        return self.estabelecimento.nome


class Caracteristica(models.Model):

    estabelecimento = models.ForeignKey('Estabelecimento',related_name='caracteristicas')
    titulo = models.CharField(max_length=100)
    conteudo = models.CharField(max_length=250)

    def __str__(self):
        return self.titulo


class Preco(models.Model):
    estabelecimento = models.ForeignKey('Estabelecimento', related_name='precos')
    titulo = models.CharField(null=True, blank=True, max_length=100)
    valor = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return '{} - {}'.format(self.titulo, self.valor)
