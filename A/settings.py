"""
Django settings for A project.
"""
from datetime import timedelta

import environ
from django.utils.translation import ugettext_lazy as _
from pathlib import Path

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent

APPS_DIR = ROOT_DIR / 'apps'
env = environ.Env()

ROOT_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if ROOT_DOT_ENV_FILE:
    # OS Environment variables that read from .env file
    env.read_env(str(ROOT_DIR / '.env'))

# GENERAL
DEBUG = env.bool('DJANGO_DEBUG', True)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "Asia/Tehran"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#languages
LANGUAGES = [("en-us", _("English"))]


# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}
DATABASES['default']["ATOMIC_REQUESTS"] = False

# URLS
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'A.urls'
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'A.wsgi.application'

# APPS
# ----------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

THIRD_PARTY_APPS = [
    'rest_framework',
    'drf_yasg',
    'rest_framework_simplejwt',
]

LOCAL_APPS = [
    'apps.accounts',
    'apps.barbers',
    'apps.reservations',
    'apps.payments',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE
# ----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

# STATIC
# ----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = ROOT_DIR / 'static'
STATIC_URL = '/static/'
s = ROOT_DIR / 'staticfiles'
STATICFILES_DIRS = [s]

MEDIA_ROOT = ROOT_DIR / 'media'
MEDIA_URL = '/media/'

# TEMPLATES
# ----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Password validation
# ----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
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

# SECRET KEY
# ---------------------------------------------------------------------------------------
SECRET_KEY = env(
    "DJANGO_SECRET_KEY"
)

# ALLOWED HOSTS
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "192.168.1.106"]

# REST FRAMEWORK CONFIG
# # -----------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.AllowAny',
#     ],
#     'DEFAULT_THROTTLE_CLASSES': [
#         'rest_framework.throttling.AnonRateThrottle',
#         'rest_framework.throttling.UserRateThrottle'
#     ],
#     'DEFAULT_THROTTLE_RATES': {
#         'anon': '100/second',
#         'user': '200/second'
#     },

# AUTH User model
# # -------------------------------
AUTH_USER_MODEL = 'accounts.User'

# CUSTOM AUTHENTICATION
# -------------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'apps.accounts.authentication.UsernameBackend',
    'django.contrib.auth.backends.ModelBackend',
)


# CELERY CONFIGURATIONS
# ------------------------------------------------------------------------------------------------
# CELERY_BROKER_URL = env('CELERY_BROKER_URL')
# CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND')
# CELERY_TASK_ALWAYS_EAGER  = True
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TASK_SERIALIZER = 'json'

# Redis
# --------------------------------------------------------------------------------------------------------
REDIS_HOST = env('REDIS_HOST')
REDIS_DB = env('REDIS_DB')
REDIS_PORT = env('REDIS_PORT')
#
# #
# SWAGGER_SETTINGS = {
#     "DEFAULT_AUTO_SCHEMA_CLASS": "apps.api.inspectors.SwaggerAutoSchema"
# }
#
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(weeks=1),
    'USER_ID_FIELD': 'username',
    'USER_ID_CLAIM': 'username',
}

