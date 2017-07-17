from django.db import models


class EnvioNewsLetter(models.Model):
    campanha = models.CharField('Nome da campanha', max_length=100, help_text='Lembrar de setar como publicado o template no Sparkpost')
    template = models.CharField('Spark Template', max_length=100)
    recipients = models.TextField('Lista de Emails', max_length=100)
    enviado = models.BooleanField('Foi enviado?', default=False)
    timestamp = models.DateTimeField('Criado em', auto_now_add=True)
    response = models.CharField('Response Spark', max_length=200)

    def __unicode__(self):
        return self.campanha

    class Meta:
        verbose_name = u'Envio de Newsletter'        
        verbose_name_plural = u'Envio de Newsletters'
