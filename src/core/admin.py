from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from src.core.models import Estabelecimento, Categoria, Telefone, Foto, Anuncio, Caracteristica, Preco


class TelefoneInLine(admin.TabularInline):
    model = Telefone
    extra = 1
    min_num = 0


class FotoInLine(admin.TabularInline):
    model = Foto
    extra = 1
    min_num = 0


class CaracteristicaInline(admin.TabularInline):
    model = Caracteristica
    extra = 1
    min_num = 0


class PrecoInline(admin.TabularInline):
    model = Preco
    extra = 1
    min_num = 0


class EstabelecimentoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
    list_display = ['nome', 'website']
    inlines = [
        FotoInLine,
        TelefoneInLine,
        CaracteristicaInline,
        PrecoInline,
    ]


class CategoriaAdmin(MPTTModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Estabelecimento, EstabelecimentoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Anuncio)

