from emergencyfood.settings.base import *

SECRET_KEY = 'django-insecure-*_4pd6)d-@vycnsob9ukyj9+cgi@%iojdjfj$+x1bjsl0f6seq'
DEBUG = True
ALLOWED_HOSTS = []

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

SASS_PROCESSOR_ROOT = STATICFILES_DIRS[0]
SASS_PRECISION = 8

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}