# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from django.shortcuts import resolve_url as r
from mptt.fields import TreeManyToManyField

from mptt.models import MPTTModel, TreeForeignKey

# @deconstructible
def path_and_rename(path):
    # path = '{}/{}/{}'
    #
    # def __init__(self, sub_path):
    #     self.sub_path = sub_path
    #     print(sub_path)
    #
    # def __call__(self, instance, filename):
    #     print('lol '+filename)
    #     if isinstance(instance, Estabelecimento):
    #         return path.format(instance.nome, self.sub_path, filename)
    #     else:
    #         return path.format(instance.estabelecimento.nome, self.sub_path, filename)

    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        fname = filename.split('.')[0]
        if isinstance(instance, Estabelecimento):
            filename = '{}/{}/{}.{}'.format(instance.nome, path, fname, ext)
        else:
            filename = '{}/{}/{}.{}'.format(instance.estabelecimento.nome, path, fname, ext)
        # return the whole path to the file
        return filename

    return wrapper


class Estabelecimento(models.Model):

    CIDADES = (
        ('E', 'Ciudad del Este'),
        ('P', 'Pedro Juan Caballero'),
        ('S', 'Salto del Guairá'),

    )
    upload_dir = path_and_rename('logo')
    nome = models.CharField(max_length=120)
    website = models.URLField()
    slug = models.SlugField(unique=True)
    logo = models.ImageField(upload_to=upload_dir, null=True)
    descricao = models.TextField()
    endereco = models.CharField(max_length=60)
    cidade = models.CharField(max_length=1, choices=CIDADES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    coordenadas = models.CharField('Coordenadas', null=True, blank=True, max_length=40)
    categoria = TreeManyToManyField('Categoria', blank=True, related_name='estabelecimentos')

    class Meta:
        verbose_name = 'Estabelecimento'
        verbose_name_plural = 'Estabelecimentos'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_latitude_longitde(self):
        return map(lambda x: float(x), self.coordenadas.split(','))

    def serializer(obj):
        latitude, longitude = obj.get_latitude_longitde()
        return dict(nome=obj.nome, latitude=latitude, longitude=longitude)

    def get_absolute_url(self):
        return r('estabelecimento_detail', slug=self.slug)


class Telefone(models.Model):
    estabelecimento = models.ForeignKey('Estabelecimento', related_name='telefones')
    numero = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.numero


class Foto(models.Model):
    upload_dir = path_and_rename('fotos')
    estabelecimento = models.ForeignKey('Estabelecimento')
    foto = models.ImageField(upload_to=upload_dir, null=True, blank=True)

    def __str__(self):
        return self.foto.name


class CategoriaManager(models.Manager):
    def principais(self, *args, **kwargs):
        return super(CategoriaManager, self).filter(parent=None)


class Categoria(MPTTModel):
    # normal parent
    # parent = models.ForeignKey('self', verbose_name='Categoria', null=True, blank=True)

    # mptt parent
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    nome = models.CharField(max_length=60)
    slug = models.SlugField()
    logo = models.ImageField(upload_to='categorias', null=True, blank=True)

    objects = CategoriaManager()

    class MPTTMeta:
        order_insertion_by = ['nome']

    def __str__(self):
        return self.nome

    # def subcategorias(self):
    #     return Categoria.objects.filter(parent=self)

    def all_children_estabelecimentos(self):
        estabelecimentos = []
        for c in self.children.all():
            for e in c.estabelecimentos.all():
                if not e in estabelecimentos:
                    estabelecimentos.append(e)
        return estabelecimentos

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    def get_absolute_url(self):
        return r('categoria_detail', slug=self.slug)


class AnuncioManager(models.Manager):
    def ativos(self, *args, **kwargs):
        return super(AnuncioManager, self).filter(ativo=True)


class Anuncio(models.Model):
    upload_dir = path_and_rename('banner')
    banner = models.ImageField(upload_to=upload_dir)
    url = models.URLField()
    estabelecimento = models.ForeignKey('Estabelecimento')
    ativo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = AnuncioManager()

    def __str__(self):
        return self.estabelecimento.nome


class Caracteristica(models.Model):

    estabelecimento = models.ForeignKey('Estabelecimento')
    titulo = models.CharField(max_length=100)
    conteudo = models.CharField(max_length=250)

    def __str__(self):
        return self.titulo


class Preco(models.Model):
    estabelecimento = models.ForeignKey('Estabelecimento')
    titulo = models.CharField(null=True, blank=True, max_length=100)
    valor = models.DecimalField(max_digits=12, decimal_places=2)


@receiver(post_delete, sender=Estabelecimento)
def estabelecimento_logo_delete(sender, **kwargs):
    estabelecimento = kwargs['instance']
    if estabelecimento.logo:
        storage, path = estabelecimento.logo.storage, estabelecimento.logo.path
        storage.delete(path)


@receiver(post_delete, sender=Foto)
def foto_delete(sender, **kwargs):
    foto = kwargs['instance']
    if foto.foto:
        storage, path = foto.foto.storage, foto.foto.path
        storage.delete(path)


@receiver(post_delete, sender=Categoria)
def categoria_logo_delete(sender, **kwargs):
    instance = kwargs['instance']
    if instance.logo:
        storage, path = instance.logo.storage, instance.logo.path
        storage.delete(path)


@receiver(post_delete, sender=Anuncio)
def anuncio_banner_delete(sender, **kwargs):
    instance = kwargs['instance']
    if instance.banner:
        storage, path = instance.banner.storage, instance.banner.path
        storage.delete(path)

