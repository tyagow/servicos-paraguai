from django.db.models.signals import post_delete
from django.dispatch import receiver

from src.core.models import Estabelecimento, Foto, Categoria, Anuncio


@receiver(post_delete, sender=Estabelecimento)
def estabelecimento_logo_delete(sender, **kwargs):
    estabelecimento = kwargs['instance']
    print('Deletando foto')
    if estabelecimento.logo:
        estabelecimento.logo.delete(False)


@receiver(post_delete, sender=Foto)
def foto_delete(sender, **kwargs):
    foto = kwargs['instance']
    if foto.foto:
        foto.foto.delete(False)


@receiver(post_delete, sender=Categoria)
def categoria_logo_delete(sender, **kwargs):
    instance = kwargs['instance']
    if instance.logo:
        instance.logo.delete(False)


@receiver(post_delete, sender=Anuncio)
def anuncio_banner_delete(sender, **kwargs):
    instance = kwargs['instance']
    if instance.banner:
        instance.banner.delete(False)