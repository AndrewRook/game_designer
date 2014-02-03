"""
Django settings for game_designer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR,os.pardir)#os.pardir is just '..' on unix/osX systems.
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
CARD_GAME_PATH = os.path.join(PROJECT_PATH, 'card_game')
USER_CONTROL_PATH = os.path.join(PROJECT_PATH, 'user_control')
PROJECT_TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
CARD_GAME_TEMPLATE_PATH = os.path.join(CARD_GAME_PATH, 'templates')
USER_CONTROL_TEMPLATE_PATH = os.path.join(USER_CONTROL_PATH, 'templates')
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')

LOGIN_URL = '/usercontrol/login/'
LOGIN_REDIRECT_URL = ''


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c%c(4^k843966tu%itov-j0x!%i1i0!3twun=0+0&^n!e9k8en'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_TEMPLATE_PATH,
    CARD_GAME_TEMPLATE_PATH,
    USER_CONTROL_TEMPLATE_PATH,
    )

STATICFILES_DIRS = (
    STATIC_PATH,
    )

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'user_control',
    'card_game',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'game_designer.urls'

WSGI_APPLICATION = 'game_designer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

CARD_GAME_DATABASE_PATH = os.path.join(CARD_GAME_PATH, 'card_game.db')
USER_CONTROL_DATABASE_PATH = os.path.join(USER_CONTROL_PATH, 'user_control.db')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': CARD_GAME_DATABASE_PATH,
    },
    'user_control': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': USER_CONTROL_DATABASE_PATH,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(CARD_GAME_PATH,'media')
