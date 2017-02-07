from .settings import *

DEBUG = False

DATABASES = {
    'default': {
        'HOST': '',
        'NAME': 'miniatures_registrar',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'mini',
        'PASSWORD': '',
        'OPTIONS': {

        },
    }
}


ALLOWED_HOSTS = ['178.62.22.84', 'polandfinlandplayground.org']

STATIC_URL = '/mini/static/'
MEDIA_URL = '/mini/media/'
