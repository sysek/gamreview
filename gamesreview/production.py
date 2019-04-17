import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'gamesreview.settings'

os.environ['DJANGO_SECRET_KEY'] = os.environ['SECRET_KEY']
application = get_wsgi_application()
