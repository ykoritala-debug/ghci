# assisted_mobility/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assisted_mobility.settings')

application = get_wsgi_application()