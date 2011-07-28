import os
import sys

path = '/srv/capistranos/dmxacl/current'
if path not in sys.path:
    sys.path.append(path)


os.environ['DJANGO_SETTINGS_MODULE'] = 'dmxacl.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

