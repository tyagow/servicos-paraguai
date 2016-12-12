from django.db import models


class AnuncioManager(models.Manager):
    def ativos(self, *args, **kwargs):
        return super(AnuncioManager, self).filter(ativo=True)


class CategoriaManager(models.Manager):
    def principais(self, *args, **kwargs):
        return super(CategoriaManager, self).filter(parent=None)


def path_and_rename_logo(instance, filename):
    return '{}/{}/{}'.format(instance.nome, 'logo', filename)


def path_and_rename_fotos(instance, filename):
    return '{}/{}/{}'.format(instance.estabelecimento.nome, 'fotos', filename)


def path_and_rename_banner(instance, filename):
    return '{}/{}/{}'.format(instance.estabelecimento.nome, 'banner', filename)


def path_and_rename_categoria(instance, filename):
    ext = filename.split('.')[-1]
    return '{}/{}_{}.{}'.format('categorias', instance.nome, 'icon', ext)

