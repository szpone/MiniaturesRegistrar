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
