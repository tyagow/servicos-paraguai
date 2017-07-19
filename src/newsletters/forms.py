from django import forms

from src.newsletters.models import EnvioNewsLetter, CadastroNewsLetter
from src.newsletters.utils import get_sparkpost_template_list, get_sparkpost_recipients_list


class NewsletterModelForm(forms.ModelForm):
    class Meta:
        fields = ['campanha','template', 'recipients', 'response',]
        model = EnvioNewsLetter

    def __init__(self, *args, **kwargs):
        super(NewsletterModelForm, self).__init__(*args, **kwargs)
        self.fields['template'] = forms.ChoiceField(choices=[(o['id'], o['name']) for o in get_sparkpost_template_list()])
        self.fields['recipients'] = forms.ChoiceField(choices=[(o['id'], o['name']) for o in get_sparkpost_recipients_list()])


class CadastroNewsLetterForm(forms.ModelForm):
    class Meta:
        model = CadastroNewsLetter