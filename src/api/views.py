import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from src.core.models import Estabelecimento


def estabelecimentos(request):
    # cidade, nome, preco, categoria = None, None, None, None
    # if 'cidade' in request.GET or 'nome' in request.GET or 'preco' in request.GET or 'categoria' in request.GET:
    cidade = request.GET.get('cidade', None)
    nome = request.GET.get('nome', None)
    preco = request.GET.get('preco', None)
    categoria = request.GET.get('categoria', None)
    cidade = Estabelecimento.get_cidade_index(cidade)
    print(request.GET)
    query_filter = Estabelecimento.objects.busca(cidade=cidade, nome=nome, preco=preco, categoria=categoria)

    serialized = list(map(lambda obj: obj.serializer(), query_filter))
    data = json.dumps(serialized, cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type="application/json")