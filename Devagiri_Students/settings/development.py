from .base import *

SECRET_KEY = 'django-insecure-udb(ffo@@meyh7j)p=#r12vb(-li&8&$3f+0$r+@z(8u51-3$j'

DEBUG = True

ALLOWED_HOSTS = ['192.168.27.52','localhost','127.0.0.1','*']

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


STATICFILES_DIRS = [
    BASE_DIR , "static",
]
