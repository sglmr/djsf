"""
Django settings for djsf project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import sys
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from environs import env

# Read environment variables
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# TESTING is True if django is running tests
TESTING = "pytest" in sys.argv[0]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", False)


ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", [])

AUTH_USER_MODEL = "djsf.AppUser"


# Application definition
INSTALLED_APPS = [
    # project apps
    "djsf",
    # third party apps
    "debug_toolbar",
    "django_browser_reload",
    "whitenoise.runserver_nostatic",
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

if not DEBUG:
    # If not in DEBUG mode, remove the debug toolbar config
    INSTALLED_APPS.remove("debug_toolbar")
    MIDDLEWARE.remove("debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["127.0.0.1"]


ROOT_URLCONF = "djsf.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "djsf.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "OPTIONS": {
            "transaction_mode": "IMMEDIATE",
            "timeout": 10,
            "init_command": """
                PRAGMA journal_mode=WAL;
                PRAGMA synchronous=NORMAL;
                PRAGMA mmap_size=134217728;
                PRAGMA journal_size_limit=67108864;
                PRAGMA cache_size=2000;
            """,
        },
    }
}
# Make the db folder if it doesn't already exist
DATABASES["default"]["NAME"].parent.mkdir(parents=True, exist_ok=True)

STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_HOST = env.str("DJANGO_STATIC_HOST", "")
STATIC_URL = STATIC_HOST + "/static/"

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Settings for Testing
if TESTING:
    DEBUG = False

    # Use memory storage
    STORAGES = {
        "default": {"BACKEND": "django.core.files.storage.InMemoryStorage"},
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

    # Use the dummy cache
    CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}

    # Make whitenoise work a little faster
    WHITENOISE_AUTOREFRESH = True

    # Use a faster password hasher
    PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

    # Keep django debug toolbar out of testing
    if "debug_toolbar" in INSTALLED_APPS:
        INSTALLED_APPS.remove("debug_toolbar")
    if "debug_toolbar.middleware.DebugToolbarMiddleware" in MIDDLEWARE:
        MIDDLEWARE.remove("debug_toolbar.middleware.DebugToolbarMiddleware")
