import json

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from src.core.models import Estabelecimento


def estabelecimentos(request):
    cidade = request.GET.get('cidade', None)
    nome = request.GET.get('nome', None)
    preco = request.GET.get('preco', None)
    categoria = request.GET.get('categoria', None)
    cidade = Estabelecimento.get_cidade_index(cidade)
    query_filter = Estabelecimento.objects.busca(cidade=cidade, nome=nome, preco=preco, categoria=categoria)
    paginator = Paginator(query_filter, settings.ESTABELECIMENTOS_POR_PAGINA)
    page = request.GET.get('page')
    try:
        query_filter = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_filter = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query_filter = paginator.page(paginator.num_pages)

    serialized = list(map(lambda obj: obj.serializer(), query_filter))
    data = json.dumps(serialized, cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type="application/json")