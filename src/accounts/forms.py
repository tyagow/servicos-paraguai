from django import forms
from django.contrib.auth import (
    get_user_model,
)
from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationFormUniqueEmail

from src.accounts.models import Profile

User = get_user_model()


class UserLoginForm(AuthenticationForm):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = UsernameField(
        label=_('Usuário'),
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': ''}),
    )
    password = forms.CharField(
        label=_("Senha"),
        strip=False,
        widget=forms.PasswordInput,
    )


class UserRegisterForm(RegistrationFormUniqueEmail):
    username = forms.CharField(
        label=_("Usuário"),
        strip=False,
        widget=forms.TextInput(attrs={'placeholder': '{}. Ex: reclama_paraguay'.format(_("Crie um nome de usuário")) }),
        error_messages={
            'invalid': _(
                _("Formato invalido de usuário, utilize: nome_sobrenome, nome.sobrenome e não utilize espaços.")
            )
        }
    )
    email2 = forms.EmailField(label=_('Confirme o email'))
    password1 = forms.CharField(
        label=_("Senha"),
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_("Confirme senha"),
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password1',
            'password2'
        ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if not email == email2:
            raise forms.ValidationError(_("Emails precisam ser identicos"))

        return email


class ProfileFormRegistration(RegistrationFormUniqueEmail):
    class Meta:
        model = Profile
        fields = ['status']
