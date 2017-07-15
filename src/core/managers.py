from decimal import Decimal
from random import randint

from django.db import models
from django.db.models import Count


class AnuncioQuerySet(models.QuerySet):
    def ativos(self, count=None):
        if not count:
            return self.filter(ativo=True)
        if count >= self.count():
            return self.filter(ativo=True)

        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.filter(ativo=True)[random_index:random_index+2]

AnuncioManager = models.Manager.from_queryset(AnuncioQuerySet)

class CategoriaManager(models.Manager):
    def principais(self, *args, **kwargs):
        return super(CategoriaManager, self).filter(parent=None)

    def is_hotel(self, *args, **kwargs):
        query = super(CategoriaManager, self).filter(nome__icontains='Hospedagem')
        return len(query) > 0


class EstabelecimentoManager(models.Manager):
    def busca(self, *args, nome=None, cidade=None, preco=None, categoria=None, **kwargs):
        queryFilter = super(EstabelecimentoManager, self).all()
        if cidade and not 'todas' in cidade:
            queryFilter = super(EstabelecimentoManager, self).filter(cidade=cidade)

        if categoria and not 'todas' in categoria:
            if queryFilter:
                queryFilter = queryFilter.filter(categoria__nome__icontains=categoria)
            else:
                queryFilter = super(EstabelecimentoManager, self).filter(categoria__nome__icontains=categoria)

        if preco:
            if queryFilter:
                queryFilter = queryFilter.filter(preco__valor__lte=Decimal(preco))
            else:
                queryFilter = super(EstabelecimentoManager, self).filter(preco__valor__lte=Decimal(preco))

        if nome:
            if queryFilter:
                queryFilter = queryFilter.filter(nome__icontains=nome)
            else:
                queryFilter = super(EstabelecimentoManager, self).filter(nome__icontains=nome)
        return queryFilter.distinct()

    def recomendados(self, *args, **kwargs):
        return super(EstabelecimentoManager, self).filter(recomendado=True)