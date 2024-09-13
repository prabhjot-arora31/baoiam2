"""
WSGI config for baoiamweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'baoiamweb.settings')
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
application = get_wsgi_application()
app  = application
