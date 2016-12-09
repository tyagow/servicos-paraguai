from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from src.core.models import Categoria, Estabelecimento, Anuncio


def home(request):
    context = {'estabelecimentos': Estabelecimento.objects.all(), 'anuncios': Anuncio.objects.ativos()}
    return render(request, 'index.html', context)


def estabelecimento_detail(request, slug):
    estabelecimento = get_object_or_404(Estabelecimento, slug=slug)
    return render(request, 'core/estabelecimento_detail.html', {'estabelecimento': estabelecimento})


def categoria_detail(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    return render(request, 'core/categoria_detail.html', {'categoria': categoria})


def busca(request):
    context = {'estabelecimentos': None}
    if 's' in request.GET:
        query = request.GET['s']
        # query_list = Estabelecimento.objects.filter(Q(nome__icontains=query) | Q(categoria__nome__icontains=query))
        query_list = Estabelecimento.objects.filter(nome__icontains=query)
        if len(query_list) == 0:
            query_list = Estabelecimento.objects.filter(categoria__nome__icontains=query)

        context = {'estabelecimentos': query_list}

    return render(request, 'core/busca_resultado.html', context)

