from django.contrib import admin

from src.newsletters.forms import NewsletterModelForm
from src.newsletters.models import EnvioNewsLetter
from src.newsletters.utils import enviar_sparkpost


def enviar_newsletter_pendentes(modeladmin, request, queryset):
    for newsletter in queryset:
        if not newsletter.enviado:
            response = enviar_sparkpost(newsletter)
enviar_newsletter_pendentes.short_description = 'Enviar Newsletter selecionada'


class EnvioNewsLetterAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'enviado', 'template', 'recipients', 'timestamp',]
    actions = [enviar_newsletter_pendentes]
    form = NewsletterModelForm
    readonly_fields = ('response', 'enviado')


admin.site.register(EnvioNewsLetter, EnvioNewsLetterAdmin)