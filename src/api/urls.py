from django.conf.urls import url
from src.api.views import estabelecimentos
urlpatterns = [
    url(r'^estabelecimentos/$', estabelecimentos, name='estabelecimentos'),
]
