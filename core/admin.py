from django.contrib import admin
from core.models import Estabelecimento, Categoria, Telefone


class TelefoneInLine(admin.TabularInline):
    model = Telefone


class EstabelecimentoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
    list_display = ['nome', 'website', 'categoria', 'plano']
    inlines = [
        TelefoneInLine,
    ]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Estabelecimento, EstabelecimentoAdmin)
admin.site.register(Categoria, CategoryAdmin)
