"""
WSGI config for sparaguai project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from dj_static import Cling, MediaCling
from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

# if settings.DEBUG:
#     application = Cling(MediaCling(get_wsgi_application()))
# else:
application = get_wsgi_application()
