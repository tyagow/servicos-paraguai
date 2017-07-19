from django import forms


class CadastroNewsLetterForm(forms.Form):
    email = forms.EmailField()
    nome = forms.CharField(max_length=120)