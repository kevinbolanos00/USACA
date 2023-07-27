from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'kevin',
        'PASSWORD': 'kevincurso',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
#STATICFILES_DIR = [BASE_DIR.child('static')]
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL='/media/'
MEDIA_ROOT = BASE_DIR / 'media'
#[BASE_DIR.child('media')]