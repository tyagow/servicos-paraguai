from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from src.tickets.forms import AnuncianteForm
from src.tickets.models import Ticket


def anunciante(request):
    form = AnuncianteForm(request.POST or None)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        conteudo = form.cleaned_data['conteudo']
        ticket = Ticket.objects.anunciante(nome, email, conteudo)
        if ticket:
            form = AnuncianteForm()
            messages.success(request, _('Solicitação registrada'))

    context = {'form': form}
    return render(request, 'tickets/seja-anunciante.html', context=context)


