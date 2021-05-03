from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
CONN_MAX_AGE = 900  # 15 minutes of persistent connection

EMAIL_FROM = ''
EMAIL_HOST = 'mail.swin.edu.au'
EMAIL_PORT = 25

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_FROM = 'ssaleheen@swin.edu.au'
EMAIL_HOST = 'mail.swin.edu.au'
EMAIL_PORT = 25

STATIC_ROOT = os.path.join(BASE_DIR, '../static-files/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../static/"),
    os.path.join(BASE_DIR, "../galaxiaweb/static/"),


    # os.path.join(BASE_DIR, "../accounts/static/"),
]

# ROOT_SUBDIRECTORY_PATH = 'projects/live/galaxia/'
ROOT_SUBDIRECTORY_PATH = ''

STATIC_URL = '/' + ROOT_SUBDIRECTORY_PATH + 'static/'
# SITE_URL = 'https://supercomputing.swin.edu.au/projects/live/galaxia'


MEDIA_URL = '/' + ROOT_SUBDIRECTORY_PATH + 'media/'

RUN_GALAXIA_COMMAND = ['galaxia', '-r']
GALAXIA_OUTPUT_DIR = os.environ['GALAXIA_OUTPUT_DIR']
GALAXIA_CODE_DATA_DIR = os.environ['GALAXIA_CODE_DATA_DIR']

try:
    from .local import *
except ImportError:
    pass
