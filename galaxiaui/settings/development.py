from .base import *
import os

DEBUG = os.environ['DEBUG']

ALLOWED_HOSTS = ['*']

SITE_URL = 'http://127.0.0.1:8000'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_FROM = os.environ['NOTIFICATION_EMAIL_FROM']
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']

for logger in LOGGING['loggers']:
    LOGGING['loggers'][logger]['handlers'] = ['console', 'file']

try:
    from .local import *
except ImportError:
    pass
