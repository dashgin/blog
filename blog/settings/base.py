from pathlib import Path
import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 's,dvnbeJHGFDniqwey32W@feF#@#rC##@E2#')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
    'posts.apps.PostsConfig',
    'contact.apps.ContactConfig',

    'widget_tweaks',
    'django.contrib.humanize',
    'tinymce',
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'posts.custom_context_processor.c_t_p_list',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'accounts.CustomUser'

# CKEDITOR CONFIG
CKEDITOR_UPLOAD_PATH = 'images/posts/%Y/%m/%d/'
CKEDITOR_BASEPATH = os.path.join(STATIC_URL, 'ckeditor/ckeditor/')
CKEDITOR_CONFIGS = {
    'toolbar': 'Basic',
    'post_content': {
        # 'skin': 'office2013',
        'skin': 'bootstrapck',
        'toolbarCanCollapse': True,
        'width': '100%',
        'tabSpaces': 4,
        'toolbar': [
            {'name': 'document',
             'items': ['Source', '-', 'Preview']},
            {'name': 'document2',
             'items': ['Save', 'NewPage', '-', 'Templates', ]},
            {'name': 'clipboard',
             'items': ['Undo', 'Redo', '-', 'Cut', 'Copy', 'Paste', '-', 'PasteText', 'PasteFromWord', ]},
            {'name': 'links',
             'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'paragraph',
             'items': ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'Iframe']},
            {'name': 'tools', 'items': ['ShowBlocks', 'CreateDiv', 'Templates']},
            '/',
            {'name': 'styles',
             'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'colors',
             'items': ['TextColor', 'BGColor']},
            {'name': 'paragraph',
             'items': ['CodeSnippet', 'Blockquote', '-', 'NumberedList', 'BulletedList', '-', 'Outdent',
                       'Indent']},
            {'name': 'max', 'items': ['Maximize']},
            '/'
        ],
        'extraPlugins': ','.join([
            'codesnippet',
        ]),
    }
}
CKEDITOR_ALLOW_NONIMAGE_FILES = False

# TINYMCE Editor config
TINYMCE_JS_URL = os.path.join(STATIC_URL, 'tinymce/tinymce.min.js')
TINYMCE_COMPRESSOR = False
TINYMCE_DEFAULT_CONFIG = {
    "height": "250px",
    "width": "100%",
    "menubar": False,
    "plugins": "emoticons autolink lists link image charmap print preview anchor searchreplace visualblocks code "
               "fullscreen insertdatetime media table paste codesample  wordcount",
    "toolbar": "undo redo | bold italic underline strikethrough | formatselect | alignleft "
               "aligncenter alignright alignjustify | outdent indent | numlist bullist | forecolor "
               "backcolor removeformat | codesample |link| charmap emoticons | fullscreen",
}

# Crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Disqus
# DISQUS_API_KEY = '7EjHlRx9yOXXeeajMPaS0Ftd9g5BzVnnJAQhMBhXfUHYosYlspVnSM71ZkpnaIfM'
# DISQUS_WEBSITE_SHORTNAME = 'disqus_BVzZuyMdnw'

# PWA
PWA_APP_NAME = 'Technology Blog'
PWA_APP_DESCRIPTION = "A blog"
PWA_APP_THEME_COLOR = '#333333'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/img/blog.png',
        'sizes': '512x512'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/img/blog.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/icons/splash-640x1136.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'


# Heroku
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())

