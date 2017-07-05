from django.contrib import admin

from src.tickets.models import TORNAR_ANUNCIANTE, Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ['status', 'tipo_completo', 'updated']
    list_filter = ['status', 'date', 'tipo']
    search_fields = ['titulo', 'descricao']
    raw_id_fields = ['criador']
    exclude = ['content_type', 'object_id']
    # fields = ['titulo', 'descricao', 'status', 'tipo', 'criador', 'c_object']

    readonly_fields = ('c_object',)

    def tipo_completo(self, obj):
        tipo_completo = obj.get_tipo_display()
        if obj.tipo == TORNAR_ANUNCIANTE:
            tipo_completo = '{} - {}'.format(obj.get_tipo_display(), obj.content_object)

        return tipo_completo

    tipo_completo.short_description = 'Tipo'

    def c_object(self, obj):
        return obj.content_object

    c_object.short_description = 'Referente'


admin.site.register(Ticket, TicketAdmin)

