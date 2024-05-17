from .base import *


with open("/home/iedc/Campus_Connect/secret_key.txt") as f:
    SECRET_KEY = f.read().strip()

DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0','devagiricampus.in','www.devagiricampus.in','localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'campusdb',
        'USER': 'campususer',
        'PASSWORD': 'campus@devagiri2023',
        'HOST': 'localhost',  
        'PORT': '5432',  
    }
}

STATIC_ROOT =  os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media/')

#HTTP settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000 #1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True