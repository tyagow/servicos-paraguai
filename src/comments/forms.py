from django import forms
from django.utils.translation import ugettext as _


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    conteudo = forms.CharField(
        label='',
        help_text=_('Escreva seu comentario'),
        required=True,
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40, 'placeholder': _('Escreva seu comentario'), 'class': 'form-control'})
    )
    nome = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': _('Digite seu nome'), 'cols': 40, 'class': 'form-control form-comments-nome'})
    )
