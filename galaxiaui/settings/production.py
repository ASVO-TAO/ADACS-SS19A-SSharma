from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
CONN_MAX_AGE = 900  # 15 minutes of persistent connection

EMAIL_FROM = os.environ['NOTIFICATION_EMAIL_FROM']
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = os.path.join(BASE_DIR, '../static-files/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../static/"),
    os.path.join(BASE_DIR, "../galaxiaweb/static/"),
]

try:
    from .local import *
except ImportError:
    pass
