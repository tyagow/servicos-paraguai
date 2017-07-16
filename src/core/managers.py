from decimal import Decimal
from random import randint

from django.db import models
from django.db.models import Count


class AnuncioQuerySet(models.QuerySet):
    def ativos(self, count=None):
        total = self.count()
        if total == 0:
            return self
        if not count:
            return self.filter(ativo=True)
        elif count > total:
            dif = count - total
            principais = list(self.all())
            index = self.aggregate(count=Count('id'))['count']
            while dif > 0:
                random_index = randint(0, index - 1)
                principais.append(self.all()[random_index])
                dif -= 1
            return principais
        else:
            index = self.aggregate(count=Count('id'))['count']
            random_index = randint(0, index - 1)
            if random_index + count >= index:
                random_index = index - count
            return self.filter(ativo=True)[random_index:random_index+count]


AnuncioManager = models.Manager.from_queryset(AnuncioQuerySet)


class CategoriaManager(models.Manager):
    def principais(self, *args, **kwargs):
        return super(CategoriaManager, self).filter(parent=None)

    def is_hotel(self, *args, **kwargs):
        query = super(CategoriaManager, self).filter(nome__icontains='Hospedagem')
        return len(query) > 0


class EstabelecimentoQuerySet(models.QuerySet):
    def busca(self, nome=None, cidade=None, preco=None, categoria=None):
        queryFilter = self.all()
        if cidade and not 'todas' in cidade:
            queryFilter = self.filter(cidade=cidade)

        if categoria and not 'todas' in categoria:
            if queryFilter:
                queryFilter = queryFilter.filter(categoria__nome__icontains=categoria)
            else:
                queryFilter = self.filter(categoria__nome__icontains=categoria)

        if preco:
            if queryFilter:
                queryFilter = queryFilter.filter(preco__valor__lte=Decimal(preco))
            else:
                queryFilter = self.filter(preco__valor__lte=Decimal(preco))

        if nome:
            if queryFilter:
                queryFilter = queryFilter.filter(nome__icontains=nome)
            else:
                queryFilter = self.filter(nome__icontains=nome)
        return queryFilter.distinct()

    def recomendados(self, count=None):
        total = self.count()
        if total == 0:
            return self
        if not count:
            return self.filter(recomendado=True)
        elif count > total:
            dif = count - total
            principais = list(self.all())
            index = self.aggregate(count=Count('id'))['count']
            while dif > 0:
                random_index = randint(0, index - 1)
                principais.append(self.all()[random_index])
                dif -= 1
            return principais
        else:
            index = self.aggregate(count=Count('id'))['count']
            random_index = randint(0, index - 1)
            if random_index + count >= index:
                random_index = index - count
            return self.filter(recomendado=True)[random_index:random_index + count]

    def mais_buscados(self, count=None):
        total = self.count()
        if total == 0:
            return self
        self = self.order_by('-search_hits')
        if not count:
            return self.all()
        elif count > total:
            dif = count - total
            principais = list(self.all())
            index = self.aggregate(count=Count('id'))['count']
            while dif > 0:
                random_index = randint(0, index - 1)
                principais.append(self.all()[random_index])
                dif -= 1
            return principais
        else:
            index = self.aggregate(count=Count('id'))['count']
            random_index = randint(0, index - 1)
            if random_index + count >= index:
                random_index = index - count
            return self[random_index:random_index + count]


EstabelecimentoManager = models.Manager.from_queryset(EstabelecimentoQuerySet)