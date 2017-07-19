from django.conf.urls import url

from src.newsletters.views import create

urlpatterns = [
    url(r'^create/$', create, name='create'),

]