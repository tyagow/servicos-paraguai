from django.forms import Form
from django.http import Http404


def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Post criado com sucesso!")
        return HttpResponseRedirect(instance.get_absolute_url())