"""
Base settings to build other settings files upon.
"""
from pathlib import Path

import environ

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# blog/
APPS_DIR = ROOT_DIR / "blog"
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "Asia/Baku"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "drf_yasg",
    "ckeditor",
]

LOCAL_APPS = [
    "blog.apps.users.apps.UsersConfig",
    "blog.apps.posts.apps.PostsConfig",
    "blog.apps.newsletter.apps.NewsletterConfig",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# AUTHENTICATION
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "blog.apps.utils.middleware.LanguageMiddleware",
]

# TEMPLATES
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [str(APPS_DIR / "templates")],
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

# STATIC
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(APPS_DIR / "static")]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
MEDIA_ROOT = str(APPS_DIR / "media")
MEDIA_URL = "/media/"

# Default auto field
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# FIXTURES
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
# FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# EMAIL
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# ADMIN
ADMIN_URL = "admin/"
ADMINS = [("""Dashgin Khudiyev""", "xudiyevdasqin7777@gmail.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
ADMIN_EMAIL = "xudiyevdasqin7777@gmail.com"
# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# django-allauth
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_ADAPTER = "blog.users.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "blog.users.adapters.SocialAccountAdapter"


# DJANGO REST FRAMEWORK
REST_FRAMEWORK = {
    "UPLOADED_FILES_USE_URL": False,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FileUploadParser",
    ],
}


# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
# CORS_URLS_REGEX = r"^/api/.*$"

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False

# CKEDITOR CONFIG
CKEDITOR_UPLOAD_PATH = "ckeditor/posts/%Y/%m/%d/"
# CKEDITOR_BASEPATH = os.path.join(STATIC_URL, 'ckeditor/ckeditor/')
CKEDITOR_CONFIGS = {
    "toolbar": "Basic",
    "post_content": {
        # 'skin': 'office2013',
        # 'skin': 'bootstrapck',
        "toolbarCanCollapse": True,
        "width": "100%",
        "tabSpaces": 4,
        "toolbar": [
            {"name": "document", "items": ["Source", "-", "Preview"]},
            {
                "name": "document2",
                "items": [
                    "Save",
                    "NewPage",
                    "-",
                    "Templates",
                ],
            },
            {
                "name": "clipboard",
                "items": [
                    "Undo",
                    "Redo",
                    "-",
                    "Cut",
                    "Copy",
                    "Paste",
                    "-",
                    "PasteText",
                    "PasteFromWord",
                ],
            },
            {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
            {
                "name": "paragraph",
                "items": [
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                ],
            },
            {
                "name": "insert",
                "items": [
                    "Image",
                    "Flash",
                    "Table",
                    "HorizontalRule",
                    "Smiley",
                    "SpecialChar",
                    "Iframe",
                ],
            },
            {"name": "tools", "items": ["ShowBlocks", "CreateDiv", "Templates"]},
            "/",
            {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
            {
                "name": "basicstyles",
                "items": [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Strike",
                    "Subscript",
                    "Superscript",
                    "-",
                    "RemoveFormat",
                ],
            },
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            {
                "name": "paragraph",
                "items": [
                    "CodeSnippet",
                    "Blockquote",
                    "-",
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Outdent",
                    "Indent",
                ],
            },
            {"name": "max", "items": ["Maximize"]},
            "/",
        ],
        "extraPlugins": ",".join(
            [
                "codesnippet",
            ]
        ),
    },
}
# CKEDITOR_ALLOW_NONIMAGE_FILES = False
