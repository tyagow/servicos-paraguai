from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from src.core.models import Estabelecimento, Categoria, Telefone, Foto


class TelefoneInLine(admin.TabularInline):
    model = Telefone
    extra = 1
    min_num = 0


class FotoInLine(admin.TabularInline):
    model = Foto
    extra = 1
    min_num = 0


class CategoriaInLine(admin.TabularInline):
    model = Categoria
    extra = 0
    min_num = 0


class EstabelecimentoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
    list_display = ['nome', 'website']
    inlines = [
        FotoInLine,
        TelefoneInLine,
    ]


class CategoriaAdmin(MPTTModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Estabelecimento, EstabelecimentoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
