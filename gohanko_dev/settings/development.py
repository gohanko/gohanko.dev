from gohanko_dev.settings.base import *

SECRET_KEY = 'django-insecure-*_4pd6)d-@vycnsob9ukyj9+cgi@%iojdjfj$+x1bjsl0f6seq'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}