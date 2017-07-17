from django.contrib import admin

from src.newsletter.forms import NewsletterModelForm
from src.newsletter.models import EnvioNewsLetter
from src.newsletter.utils import enviar_sparkpost


def enviar_newsletter_pendentes(modeladmin, request, queryset):
    for newsletter in queryset:
        if not newsletter.enviado:
            response = enviar_sparkpost(newsletter)
enviar_newsletter_pendentes.short_description = 'Enviar Newsletter selecionada'


class EnvioNewsLetterAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'enviado', 'template', 'recipients', 'timestamp',]
    actions = [enviar_newsletter_pendentes]
    form = NewsletterModelForm
    readonly_fields = ('response', 'enviado')


admin.site.register(EnvioNewsLetter, EnvioNewsLetterAdmin)