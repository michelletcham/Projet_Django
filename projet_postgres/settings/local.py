from .base import *
from .base import config

DEBUG = True
# ALLOWED_HOSTS = ['localhost']
DATABASES = {
    'default': {
       # 'ENGINE': 'django.db.backends.postgresql','django.contrib.gis.db.backends.postgis',
        'NAME': config("DATABASE_NAME"),
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': config("DATABASE_USER"),
        'PASSWORD': config("DATABASE_PASSWORD"),
        'HOST': config("DATABASE_HOST"),
        'PORT': config("DATABASE_PORT")
    }
}
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework', 
    'django_postgres', 
]