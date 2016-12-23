"""sparaguai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.i18n import set_language

from src.core.views import home, estabelecimento_detail, categoria_detail, categorias

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^estabelecimento/(?P<slug>[\w-]+)$', estabelecimento_detail, name='estabelecimento_detail'),
    url(r'^categorias/(?P<slug>[\w-]+)$', categoria_detail, name='categoria_detail'),
    url(r'^categorias/$', categorias, name='categorias'),
    url(r'^api/', include('src.api.urls', namespace='api')),
    url(r'^admin/', admin.site.urls),

]
