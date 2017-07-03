from django.conf.urls import url

from src.tickets.views import anunciante

urlpatterns = [
    url(r'^seja-anunciante/$', anunciante, name='anunciante'),

]