import urllib

from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, resolve_url

# Create your views here.

from src.core.models import Categoria, Estabelecimento, Anuncio
from django.utils.translation import ugettext as _


def home(request):
    print(_("Welcome!"))
    cidades = [cidade[1] for cidade in Estabelecimento.CIDADES]

    cidade = request.GET.get('cidade', None)
    nome = request.GET.get('nome', None)
    preco = request.GET.get('preco', None)
    categoria = request.GET.get('categoria', None)
    cidade = Estabelecimento.get_cidade_index(cidade)
    valid_querystring = {k: v for k, v in request.GET.dict().items() if v}
    if valid_querystring != request.GET.dict():
        encoded_querystring = '?' + urllib.parse.urlencode(valid_querystring)
        return HttpResponseRedirect(resolve_url('home') + encoded_querystring)

    query_estabelecimento = Estabelecimento.objects.busca(cidade=cidade, nome=nome, preco=preco, categoria=categoria)

    context = {'estabelecimentos': query_estabelecimento, 'anuncios': Anuncio.objects.ativos(), 'cidades': cidades, 'categorias': Categoria.objects.all()}
    return render(request, 'index.html', context)


def estabelecimento_detail(request, slug):
    estabelecimento = get_object_or_404(Estabelecimento, slug=slug)
    template_to_render = 'core/estabelecimento_detail.html'
    if len(estabelecimento.categoria.filter(nome__icontains='Hospedagem')) > 0:
        template_to_render = 'core/hotel_detail.html'
    return render(request, template_to_render, {'estabelecimento': estabelecimento})


def categoria_detail(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    return render(request, 'core/categoria_detail.html', {'categoria': categoria})


def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'core/categorias.html', {'categorias': categorias})

