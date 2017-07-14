import urllib

from django.conf import settings
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, resolve_url
from django.utils.translation import ugettext as _
from star_ratings import app_settings
from star_ratings.models import Rating

from src.comments.forms import CommentForm
from src.comments.models import Comment
from src.core.models import Categoria, Estabelecimento, Anuncio
from src.posts.models import Post


def home(request):

    query_estabelecimento = Estabelecimento.objects.all()

    noticias = Post.objects.noticias().principais()

    recomendados = Estabelecimento.objects.recomendados()


    context = {
        'estabelecimentos': query_estabelecimento,
        'noticias': noticias,
        'recomendados': recomendados
    }
    return render(request, 'index.html', context)


def busca(request):
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

    parametros = ''
    for item, value in request.GET.dict().items():
        if not item == 'page':
            parametros += '&{}={}'.format(item, value)
    parametros = parametros.replace(' ', '+')
    query_estabelecimento = Estabelecimento.objects.busca(cidade=cidade, nome=nome, preco=preco, categoria=categoria)

    paginator = Paginator(query_estabelecimento, settings.ESTABELECIMENTOS_POR_PAGINA)
    page = request.GET.get('page')
    try:
        query_estabelecimento = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_estabelecimento = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query_estabelecimento = paginator.page(paginator.num_pages)

    context = {
        'estabelecimentos': query_estabelecimento,
        'anuncios': Anuncio.objects.ativos(),
        'cidades': cidades,
        'categorias': Categoria.objects.all(),
        'parametros': parametros
    }
    return render(request, 'core/resultado_busca.html', context)


def estabelecimento_detail(request, slug):
    instance = get_object_or_404(Estabelecimento, slug=slug)
    template_to_render = 'core/estabelecimento_detail.html'
    if instance.is_hotel:
        template_to_render = 'core/hotel_detail.html'
    comments = instance.comments
    paginator = Paginator(comments, 6)
    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comments = paginator.page(paginator.num_pages)

    initial_data = {
        'content_type': instance.get_content_type,
        'object_id': instance.id,
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get('content_type').lower()
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('content')
        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data
        )
        if created:
            form = CommentForm(None, initial=initial_data)
            messages.success(request, _('Seu comentário será moderado e adicionado em breve.'))

    stars = [i for i in range(1, app_settings.STAR_RATINGS_RANGE + 1)]
    rating = Rating.objects.for_instance(instance)

    context = {
        'estabelecimento': instance,
        'comments': comments,
        'form': form,
        'coordenadas': instance.get_coordenadas,
        'stars': stars,
        'rating': rating,
    }
    return render(request, template_to_render, context)


def categoria_detail(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    return render(request, 'core/categoria_detail.html', {'categoria': categoria})


def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'core/categorias.html', {'categorias': categorias})
