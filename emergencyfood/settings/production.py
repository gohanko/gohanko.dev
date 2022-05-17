import os

from emergencyfood.settings.base import *
from emergencyfood.settings.development import DATABASES, SECRET_KEY

SECRET_KEY = os.environ.get('SECRET_KEY', 'adsdadasd')
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/emergencyfood.dev/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/emergencyfood.dev/media/'

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.environ.get('POSTGRESS_NAME'),
       'USER': os.environ.get('POSTGRESS_USER'),
       'PASSWORD': os.environ.get('POSTGRESS_PASSWORD'),
       'HOST': 'db',
       'PORT': 5432,
   }
}