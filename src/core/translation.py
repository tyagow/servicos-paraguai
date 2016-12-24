from modeltranslation.translator import translator, TranslationOptions
from src.core.models import Estabelecimento, Caracteristica, Preco, Categoria


class EstabelecimentoTranslationOptions(TranslationOptions):
    fields = ('descricao',)


class CaracteristicaTranslationOptions(TranslationOptions):
    fields = ('titulo', 'conteudo')


class PrecoTranslationOptions(TranslationOptions):
    fields = ('titulo', )


class CategoriaTranslationOptions(TranslationOptions):
    fields = ('nome', )


translator.register(Estabelecimento, EstabelecimentoTranslationOptions)
translator.register(Caracteristica, CaracteristicaTranslationOptions)
translator.register(Preco, PrecoTranslationOptions)
translator.register(Categoria, CategoriaTranslationOptions)

