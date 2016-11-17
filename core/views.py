from django.shortcuts import render

# Create your views here.

from core.models import Categoria


def home(request):
    context = {'categorias': Categoria.objects.all()}
    return render(request, 'index.html', context)