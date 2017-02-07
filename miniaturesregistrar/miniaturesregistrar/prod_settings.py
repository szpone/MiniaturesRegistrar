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


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

ALLOWED_HOSTS = ['178.62.22.84', 'polandfinlandplayground.org']

STATIC_URL = '/mini/static/'
MEDIA_URL = '/mini/images/'

LOGIN_URL = '/mini/login/'
LOGIN_REDIRECT_URL = '/mini/'
