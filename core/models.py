# -*- coding: utf-8 -*-
import json
import urllib.parse
import urllib.request
from django.db.models.signals import pre_save
from decimal import Decimal
from django.db import models
from django.dispatch import receiver
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
    logo = models.ImageField(null=True)
    descricao = models.TextField()
    endereco = models.CharField(max_length=60)
    cidade = models.CharField(max_length=1, choices=CIDADES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    categoria = models.ForeignKey('Categoria', null=True, blank=True)
    lat = models.DecimalField(decimal_places=7, max_digits=9, null=True, blank=True)
    long = models.DecimalField(decimal_places=7, max_digits=9, null=True, blank=True)

    class Meta:
        verbose_name = 'Estabelecimento'
        verbose_name_plural = 'Estabelecimentos'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return r('estabelecimento_detail', slug=self.slug)

    def geocode(self, address):
        address = urllib.parse.quote_plus(address)
        maps_api_url = "?".join(["http://maps.googleapis.com/maps/api/geocode/json", urllib.parse.urlencode({"address": address, "sensor":False})])
        html = ""
        _address = "?".join(["http://maps.googleapis.com/maps/api/geocode/json", urllib.parse.urlencode({"address": address, "sensor": False})])
        with urllib.request.urlopen(_address) as response:
            html = response.read()
        data = json.loads(html.decode('utf8'))

        if data['status'] == 'OK':
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']
            return Decimal(lat), Decimal(lng)
        else:
            return Decimal(0.00), Decimal(0.00)


@receiver(pre_save, sender=Estabelecimento)
def pre_save_handler(sender, instance, *args, **kwargs):
    self = instance
    if not self.lat or not self.lng:
        self.lat, self.lng = self.geocode(self.endereco)


class Telefone(models.Model):
    estabelecimento = models.ForeignKey('Estabelecimento', related_name='telefone')
    numero = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.numero


class Foto(models.Model):
    estabelecimento = models.ForeignKey('Estabelecimento')
    foto = models.ImageField(null=True, blank=True)


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

