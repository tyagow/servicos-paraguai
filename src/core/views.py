from django.shortcuts import render, get_object_or_404

# Create your views here.

from src.core.models import Categoria, Estabelecimento, Anuncio


def home(request):
    cidades = [cidade[1] for cidade in Estabelecimento.CIDADES]

    if request.GET.get('cidade'):
        cidade = request.GET['cidade']
        nome = request.GET['s']
        preco = request.GET['preco']
        categoria = request.GET['categoria']
        cidade = Estabelecimento.get_cidade_index(cidade)
        query_estabelecimento = Estabelecimento.objects.busca(cidade=cidade, nome=nome, preco=preco, categoria=categoria)
    else:
        query_estabelecimento = Estabelecimento.objects.all()
    context = {'estabelecimentos': query_estabelecimento, 'anuncios': Anuncio.objects.ativos(), 'cidades': cidades, 'categorias': Categoria.objects.all()}
    return render(request, 'index.html', context)


def estabelecimento_detail(request, slug):
    estabelecimento = get_object_or_404(Estabelecimento, slug=slug)
    return render(request, 'core/estabelecimento_detail.html', {'estabelecimento': estabelecimento})


def categoria_detail(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    return render(request, 'core/categoria_detail.html', {'categoria': categoria})


def categorias(request):
    categoria = Categoria.objects.all()
    return render(request, 'core/categorias.html', {'categorias': categoria})

