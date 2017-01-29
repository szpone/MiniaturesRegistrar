from .settings import *

DEBUG = False

DATABASES = {
    'default': {
        'HOST': '127.0.0.1',
        'NAME': 'miniatures_registrar',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'mini',
        'PASSWORD': '',
        'OPTIONS': {

        },
    }
}
