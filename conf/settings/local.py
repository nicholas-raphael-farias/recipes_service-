"""
Local settings
"""
# pylint: disable=wildcard-import, relative-beyond-top-level, undefined-variable, unused-wildcard-import
import os
from .base import *

ENV = 'local'
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'rw)z^4@w6z+g!%5(wk!a3qor)+_ag273b8_^s2n%t31pqp@plq')

# Wildcard for CORS config, remove it on Production settings
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME', ),
        'USER': os.getenv('DB_USER', ),
        'PASSWORD': os.getenv('DB_PASSWORD',),
        'HOST': os.getenv('DB_HOST', ),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
