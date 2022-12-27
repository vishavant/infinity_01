"""
WSGI config for infinity_01 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

#adding pythonanywhere project directory
project_home = '/home/vishavant/vishal'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infinity_01.settings')

application = get_wsgi_application()



# To use your own django app use code like this:
# import os
# import sys
#
## assuming your django settings file is at '/home/vishavant/mysite/mysite/settings.py'
## and your manage.py is is at '/home/vishavant/mysite/manage.py'
#path = '/home/vishavant/mysite'
#if path not in sys.path:
#    sys.path.append(path)
#
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
## then:
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()