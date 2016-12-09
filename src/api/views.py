import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from src.core.models import Estabelecimento


def estabelecimentos(request):
    es = Estabelecimento.objects.all()
    serialized = list(map(lambda obj: obj.serializer(), es))
    data = json.dumps(serialized, cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type="application/json")