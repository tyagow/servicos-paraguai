from django.db import models
from django.shortcuts import resolve_url as r
from core.managers import CategoryManager


class Estabelecimento(models.Model):

    CIDADES = (
        ('E', 'Ciudad del Este'),
        ('P', 'Pedro Juan Caballero'),
        ('S', 'Salto del Guairá'),

    )
    nome = models.CharField(max_length=120)
    website = models.URLField()
    slug = models.SlugField(unique=True)
    logo = models.ImageField()
    descricao = models.TextField()
    endereco = models.CharField(max_length=60)
    cidade = models.CharField(max_length=1, choices=CIDADES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    categoria = models.ForeignKey('Categoria', null=True, blank=True)

    class Meta:
        verbose_name = 'Estabelecimento'
        verbose_name_plural = 'Estabelecimentos'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return r('estabelecimento_detail', slug=self.slug)


class Telefone(models.Model):
    estabelecimento = models.ForeignKey('Estabelecimento', related_name='telefone')
    numero = models.CharField(max_length=15)

    def __str__(self):
        return self.numero


class Foto(models.Model):
    estabelecimento = models.ForeignKey('Estabelecimento')
    foto = models.ImageField()


class Categoria(models.Model):
    parent = models.ForeignKey('self', verbose_name='Categoria', null=True, blank=True)
    nome = models.CharField(max_length=60)
    slug = models.SlugField()
    logo = models.ImageField(null=True, blank=True)

    objects = CategoryManager()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

    def subcategorias(self):
        return Categoria.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    def get_absolute_url(self):
        return r('categoria_detail', slug=self.slug)
