import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from src.core.models import Estabelecimento


def estabelecimentos(request):
    cidade, nome, preco, categoria = None, None, None, None
    if not 'undefined' in request.GET.get('cidade'):
        cidade = request.GET['cidade']
        nome = request.GET['s']
        preco = request.GET['preco']
        categoria = request.GET['categoria']
        cidade = Estabelecimento.get_cidade_index(cidade)

    queryFilter = Estabelecimento.objects.busca(cidade=cidade, nome=nome, preco=preco, categoria=categoria)

    serialized = list(map(lambda obj: obj.serializer(), queryFilter))
    data = json.dumps(serialized, cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type="application/json")