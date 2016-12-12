from decimal import Decimal
from django.db import models


class AnuncioManager(models.Manager):
    def ativos(self, *args, **kwargs):
        return super(AnuncioManager, self).filter(ativo=True)


class CategoriaManager(models.Manager):
    def principais(self, *args, **kwargs):
        return super(CategoriaManager, self).filter(parent=None)


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
