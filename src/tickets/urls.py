from django.conf.urls import url

from src.tickets.views import anunciante, cadastrar_empresa

urlpatterns = [
    url(r'^seja-anunciante/$', anunciante, name='anunciante'),
    url(r'^cadastrar-empresa/$', cadastrar_empresa, name='cadastrar-empresa'),

]