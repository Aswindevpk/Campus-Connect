import os
from pathlib import Path
from .base import *
from dotenv import load_dotenv

# 1. Load the production environment variables
load_dotenv()

# Read the deployment SECRET_KEY (Fails explicitly if missing)
SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("CRITICAL: SECRET_KEY environment variable is missing on this production node!")

# Absolute security imperative for production
DEBUG = False

# Explicitly define your domain variants. Never leave a wildcard '*' active here.
ALLOWED_HOSTS = ['*']

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

# 2. --- DYNAMIC DATABASE SWITCHER (PSQL vs SQLITE) ---
if os.getenv('DB_NAME'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),  
            'USER': os.getenv('DB_USER'),  
            'PASSWORD': os.getenv('DB_PASSWORD'), 
            'HOST': os.getenv('DB_HOST', '127.0.0.1'),
            'PORT': os.getenv('DB_PORT', '5432'),
            # Performance optimization: Keeps database connections alive
            'CONN_MAX_AGE': 600, 
        }
    }
else:
    # Safe fallback to local SQLite if PostgreSQL env variables are absent
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# 3. --- BARE-METAL LOCAL STORAGE (Nginx Direct Handshake) ---
# No S3. Django will store files directly on your server's SSD inside the project root.
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# 4. --- PRODUCTION HTTP & GATEWAY SECURITY HARDENING ---
# Tells Django to look for the header Nginx sends to confirm the transmission was secure
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

# Cookie Security (Prevent Session hijacking over public connections)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HTTP Strict Transport Security (HSTS Rules)
SECURE_HSTS_SECONDS = 31536000  # 1 Full Year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True


# 5. --- LOGGING ENGINE ARCHITECTURE ---
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'production_errors.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}