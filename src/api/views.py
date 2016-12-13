import json

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

    serialized = list(map(lambda obj: obj.serializer(), query_filter))
    data = json.dumps(serialized, cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type="application/json")