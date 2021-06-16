from .base import *

import django_heroku
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['*']

django_heroku.settings(locals())
