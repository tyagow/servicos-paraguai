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

from src.core.views import home, estabelecimento_detail, categoria_detail, categorias, busca


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += [
    url(r'^$', home, name='home'),
    url(r'^busca/$', busca, name='busca'),
    url(r'^estabelecimento/(?P<slug>[\w-]+)$', estabelecimento_detail, name='estabelecimento_detail'),
    url(r'^estabelecimento/$', home, name='estabelecimentos'),
    url(r'^categorias/$', categorias, name='categorias'),
    url(r'^api/', include('src.api.urls', namespace='api')),
    url(r'^tickets/', include('src.tickets.urls', namespace='tickets')),
    url(r'^noticia/', include('src.posts.urls', namespace='noticias')),
    url(r'^newsletters/', include('src.newsletters.urls', namespace='newsletters')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^categorias/(?P<slug>[\w-]+)/$', categoria_detail, name='categoria_detail'),

    # url(r'^password/change/$',
    #     auth_views.password_change,
    #     name='password_change'),
    # url(r'^password/change/done/$',
    #     auth_views.password_change_done,
    #     name='password_change_done'),
    # url(r'^password/reset/$',
    #     auth_views.password_reset,
    #     name='password_reset'),
    # url(r'^password/reset/done/$',
    #     auth_views.password_reset_done,
    #     name='password_reset_done'),
    # url(r'^password/reset/complete/$',
    #     auth_views.password_reset_complete,
    #     name='password_reset_complete'),
    # url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    #     auth_views.password_reset_confirm,
    #     name='password_reset_confirm'),
    # url(r'^accounts/profile/(?P<pk>[0-9]+)/update/$', UserProfileUpdate.as_view(), name='user_profile_update'),
    # url(r'^accounts/profile/(?P<slug>[\w-]+)/$', UserProfileDetail.as_view(), name='user_profile'),
    # url(r'^accounts/profile/$', profile, name='my_user_profile'),
    # url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    # url(r'^accounts/login/$', login, name='auth_login'),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--


    url(r'^admin/', admin.site.urls),

]
