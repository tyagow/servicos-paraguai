from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


STATUS_CHOICES = getattr(settings, 'TICKETS_STATUS_CHOICES', (
    (0, _("Nova")),
    (1, _("Em Progresso")),
    (2, _("Resolvida")),
    (3, _("Fechada")),
))


TIPO_CHOICES = getattr(settings, 'TICKETS_TIPO_CHOICES', (
    (0, _("Tornar-se Anunciante")),
    (1, _("Cadastrar Empresa")),

))

TORNAR_ANUNCIANTE = 0
CADASTRAR_EMPRESA = 1

class TicketManager(models.Manager):
    def anunciante(self, nome, email, _descricao, user):
        titulo = "{} - {}  ( {} )".format(TIPO_CHOICES[0][1], nome, email)
        descricao = _descricao
        ticket = Ticket(
            criador=user,
            titulo=titulo,
            descricao=descricao,
            tipo=TORNAR_ANUNCIANTE,
        )
        ticket.save()
        return ticket

    def cadastro_empresa(self, empresa, email, descricao, user):
        titulo = '{} - {}'.format(TIPO_CHOICES[1][1], email)
        if not descricao:
            descricao = _('O usuário {usr} solicitou o cadastro da empresa {emp}.').format(usr=user, emp=empresa)
        else:
            descricao = ('O usuário {usr} solicitou o cadastro da empresa {emp}. {des}'.format(usr=user, emp=empresa, des=descricao))
        ticket = Ticket(
            criador=user,
            titulo=titulo,
            descricao=descricao,
            tipo=CADASTRAR_EMPRESA
        )
        ticket.save()
        return ticket


class Ticket(models.Model):
    criador = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Criador"), related_name='tickets', null=True, blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    date = models.DateTimeField(_("Date"), auto_now_add=True)
    updated = models.DateTimeField(_("Update"), auto_now=True)
    titulo = models.CharField(_("Titulo"), max_length=255)
    descricao = models.TextField(_("Descrição"))
    status = models.SmallIntegerField(_("Status"), choices=STATUS_CHOICES, default=0)
    tipo = models.SmallIntegerField(_("Tipo"), choices=TIPO_CHOICES, default=0)

    objects = TicketManager()

    class meta:
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")
        ordering = ['date']

    def __str__(self):
        return '{}#{}@{}'.format(self.get_tipo_display(), self.criador, self.date)

