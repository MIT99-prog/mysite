"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', "mysite.settings.local")
if os.environ.get('ENV_NAME') == 'prod':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "mysite.settings.production")
    print('setdefault production.py')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "mysite.settings.local")
    print('setdefault local.py')

application = get_wsgi_application()
