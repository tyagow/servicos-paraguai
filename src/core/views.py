from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from src.core.models import Categoria, Estabelecimento


def home(request):
    context = {'nodes': Categoria.objects.all()}
    return render(request, 'index.html', context)


def estabelecimento_detail(request, slug):
    estabelecimento = get_object_or_404(Estabelecimento, slug=slug)
    return render(request, 'core/estabelecimento_detail.html', {'estabelecimento': estabelecimento})


def categoria_detail(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    estabelecimentos = Estabelecimento.objects.filter(categoria=categoria)
    return render(request, 'core/categoria_detail.html', {'categoria': categoria})


def busca(request):
    context = {'estabelecimentos': None}
    if 's' in request.GET:
        context = {'estabelecimentos': Estabelecimento.objects.filter(nome__icontains=request.GET['s'])}

    return render(request, 'core/busca_resultado.html', context)

