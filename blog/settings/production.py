from .base import *

DEBUG = False
# DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', 'dashgin.herokuapp.com', 'dashgin.me', 'www.dashgin.me']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require'
        }
    }
}


# Files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
