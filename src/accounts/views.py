from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login
from django.contrib.auth import (
    logout,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import deprecate_current_app
from django.core.paginator import EmptyPage, Paginator
from django.core.paginator import PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, resolve_url
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import DetailView
from django.views.generic import UpdateView
from registration.backends.simple.views import RegistrationView

from src.accounts.mixins import UserPassesTestMixin
from src.accounts.models import Profile
from .forms import UserLoginForm, UserRegisterForm


def logout_view(request):
    logout(request)
    return redirect('/')


class UserProfileUpdate(UpdateView):
    model = Profile
    fields = ('status',)


def profile(request):
    return redirect('core:home')


@method_decorator(login_required, name='dispatch')
class UserProfileDetail(UserPassesTestMixin, DetailView):
    model = Profile


class MyRegistrationView(RegistrationView):

    form_class = UserRegisterForm
    success_url = '/'


def _get_login_redirect_url(request, redirect_to):
    # Ensure the user-originating redirection URL is safe.
    if not is_safe_url(url=redirect_to, host=request.get_host()):
        return resolve_url(settings.LOGIN_REDIRECT_URL)
    return redirect_to


@deprecate_current_app
@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=UserLoginForm,
          extra_context=None, redirect_authenticated_user=False):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name, request.GET.get(redirect_field_name, ''))

    if redirect_authenticated_user and request.user.is_authenticated:
        redirect_to = _get_login_redirect_url(request, redirect_to)
        if redirect_to == request.path:
            raise ValueError(
                "Redirection loop for authenticated user detected. Check that "
                "your LOGIN_REDIRECT_URL doesn't point to a login page."
            )
        return HttpResponseRedirect(redirect_to)
    elif request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return HttpResponseRedirect(_get_login_redirect_url(request, redirect_to))
    else:
        form = authentication_form(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)