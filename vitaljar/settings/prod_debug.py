from vitaljar.settings.base import *
import django_heroku
django_heroku.settings(locals())

DEBUG = True

# Tener cuidado, esto solo es seguro en heroku
ALLOWED_HOSTS = ['*']

DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'

DROPBOX_OAUTH2_TOKEN = os.getenv('DROPBOX_OAUTH2_TOKEN')
DROPBOX_ROOT_PATH = os.getenv('DROPBOX_ROOT_PATH')

SECURE_SSL_REDIRECT  =  True
SECURE_PROXY_SSL_HEADER  = ('HTTP_X_FORWARDED_PROTO' , 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'