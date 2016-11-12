from django.shortcuts import render

# Create your views here.

from core.models import Category


def home(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'index.html', context)