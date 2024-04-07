from .base import*

SECRET_KEY = 'django-insecure-vt=vjo!ju7%%#^f_0nrxlqtneg*+2@%kl4=i^hu9*-s6=sm!1-'


DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS =['basestatic/']

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'