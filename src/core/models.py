# -*- coding: utf-8 -*-

from django.db import models
from django.shortcuts import resolve_url as r
from mptt.fields import TreeManyToManyField

from mptt.models import MPTTModel, TreeForeignKey


def path_and_rename(path):
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
    nome = models.CharField(max_length=120)
    website = models.URLField()
    slug = models.SlugField(unique=True)
    logo = models.ImageField(upload_to=path_and_rename('logo'), null=True)
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

    # def geocode(self, address):
    #     address = urllib.parse.quote_plus(address)
    #     maps_api_url = "?".join(["http://maps.googleapis.com/maps/api/geocode/json", urllib.parse.urlencode({"address": address, "sensor":False})])
    #     html = ""
    #     _address = "?".join(["http://maps.googleapis.com/maps/api/geocode/json", urllib.parse.urlencode({"address": address, "sensor": False})])
    #     with urllib.request.urlopen(_address) as response:
    #         html = response.read()
    #     data = json.loads(html.decode('utf8'))
    #
    #     if data['status'] == 'OK':
    #         lat = data['results'][0]['geometry']['location']['lat']
    #         lng = data['results'][0]['geometry']['location']['lng']
    #         return Decimal(lat), Decimal(lng)
    #     else:
    #         return Decimal(0.00), Decimal(0.00)


# @receiver(pre_save, sender=Estabelecimento)
# def pre_save_handler(sender, instance, *args, **kwargs):
#     print('pre save' + instance.nome)


class Telefone(models.Model):
    estabelecimento = models.ForeignKey('Estabelecimento', related_name='telefones')
    numero = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.numero


class Foto(models.Model):
    estabelecimento = models.ForeignKey('Estabelecimento')
    foto = models.ImageField(upload_to=path_and_rename('fotos'), null=True, blank=True)

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
    banner = models.ImageField(upload_to=path_and_rename('banner'))
    url = models.URLField()
    estabelecimento = models.ForeignKey('Estabelecimento')
    ativo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = AnuncioManager()

    def __str__(self):
        return self.estabelecimento.nome
