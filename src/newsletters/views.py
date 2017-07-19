import requests
from django.forms import Form
from django.http import Http404, HttpResponseRedirect


def create(request):
    if request.method == 'POST':
        form = Form(request.POST or None, request.FILES or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            next = request.GET.get('next')
            url_action = 'http://www.comprasparaguai.com.br/newsletter/clique/?campanha=nav_guiaparaguai&origem=nav_guiaparaguai&email=' + email
            request_url(url_action)
            if next:
                return HttpResponseRedirect(next)
            return HttpResponseRedirect('/')
    else:
        raise Http404


def request_url(urlData):
    from requests.exceptions import HTTPError
    try:
        r = requests.get(urlData)
        r.raise_for_status()
    except HTTPError:
        pass