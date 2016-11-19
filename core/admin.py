from django.contrib import admin
from core.models import Estabelecimento, Categoria, Telefone, Foto


class TelefoneInLine(admin.TabularInline):
    model = Telefone
    extra = 1
    min_num = 0


class FotoInLine(admin.TabularInline):
    model = Foto
    extra = 1
    min_num = 0


class EstabelecimentoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
    exclude = ['lat', 'long']
    list_display = ['nome', 'website', 'categoria']
    inlines = [
        FotoInLine,
        TelefoneInLine,
    ]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Estabelecimento, EstabelecimentoAdmin)
admin.site.register(Categoria, CategoryAdmin)
