from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from src.tickets.forms import AnuncianteForm, CadastroEmpresaForm
from src.tickets.models import Ticket


def anunciante(request):
    form = AnuncianteForm(request.POST or None)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        conteudo = form.cleaned_data['conteudo']
        ticket = Ticket.objects.anunciante(nome, email, conteudo, request.user)
        if ticket:
            messages.success(request, _('Solicitação registrada'))
            return HttpResponseRedirect('/')

    context = {'form': form}
    return render(request, 'core/widgets/form_view.html', context=context)


def cadastrar_empresa(request):
    form = CadastroEmpresaForm(request.POST or None)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        conteudo = form.cleaned_data['conteudo']
        ticket = Ticket.objects.cadastro_empresa(nome, email, conteudo, request.user)
        if ticket:
            messages.success(request, _('Solicitação registrada'))
            return HttpResponseRedirect('/')

    context = {'form': form}
    return render(request, 'core/widgets/form_view.html', context=context)


