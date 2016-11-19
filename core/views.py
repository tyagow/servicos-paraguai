from django.shortcuts import render, get_object_or_404

# Create your views here.

from core.models import Categoria, Estabelecimento


def home(request):
    context = {'categorias': Categoria.objects.all()}
    return render(request, 'index.html', context)


def estabelecimento_detail(request, slug):
    estabelecimento = get_object_or_404(Estabelecimento, slug=slug)
    return render(request, 'core/estabelecimento_detail.html', {'estabelecimento': estabelecimento})
