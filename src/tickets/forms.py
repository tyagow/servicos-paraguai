from django import forms
from django.utils.translation import ugettext as _


class AnuncianteForm(forms.Form):
    nome = forms.CharField(
        label=_('Nome'),
        required=True,
        widget=forms.TextInput(attrs={'placeholder': _('Digite seu nome'), 'cols': 40, 'class': 'form-control'})
    )
    email = forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': _('Digite seu email'), 'class': 'form-control'})

    )
    conteudo = forms.CharField(
        label=_('Mensagem'),
        required=True,
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40, 'placeholder': _('Escreva uma mensagem ou aguarde nosso contato via email'), 'class': 'form-control'})
    )


class CadastroEmpresaForm(forms.Form):
    nome = forms.CharField(
        label=_('Nome'),
        required=True,
        widget=forms.TextInput(attrs={'placeholder': _('Digite o nome da empresa'), 'cols': 40, 'class': 'form-control'})
    )
    email = forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': _('Digite seu email'), 'class': 'form-control'})

    )
    conteudo = forms.CharField(
        label=_('Mensagem'),
        required=True,
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40, 'placeholder': _('Escreva uma mensagem com contatos da empresa como endereço, cidade, site, etc'), 'class': 'form-control'})
    )

