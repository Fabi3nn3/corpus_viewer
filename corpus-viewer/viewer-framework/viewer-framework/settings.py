# CUSTOM SETTINGS

DASHBOARD_AVAILABLE = True

"""
Django settings for viewer-framework project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATH_FILES_SETTINGS = os.path.join(BASE_DIR, '..', 'settings')

PATH_FILES_CACHE = os.path.join(BASE_DIR, '..', 'cache')

PATH_FILES_INDEX = os.path.join(BASE_DIR, '..', 'index')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hsh3+=^3d8bk+)6q@99g&z)!&9hv06*(1a7h&!3@y9d1wz$!i7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'web_page_annotation.apps.WebPageAnnotationConfig',
    'viewer.apps.ViewerConfig',
    'dashboard.apps.DashboardConfig',
    'example_app.apps.ExampleAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize'
]

MIDDLEWARE = [
    # 'viewer-framework.middleware.MultiPortMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'viewer-framework.middleware.SqlPrintMiddleware',
]

ROOT_URLCONF = 'viewer-framework.urls'

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

CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
    #     'LOCATION': 'my_cache_table',
    #     'TIMEOUT': None,
    # }
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': PATH_FILES_CACHE,
        # 'LOCATION': '/home/yiro4618/Documents/hiwi/wstud-viewer-framework-django/cache',
        'TIMEOUT': None,
    }
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #     'LOCATION': '127.0.0.1:11211',
    #     'TIMEOUT': None,
    # }
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #     'LOCATION': 'unique-snowflake',
    #     'TIMEOUT': None,
    # }
}

WSGI_APPLICATION = 'viewer-framework.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 'some_postgresql_database': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'HOST': 'localhost',
    #     'PASSWORD': 'password',
    #     'NAME': 'databasename',
    #     'USER': 'user',
    # }
}
DATABASE_ROUTERS = ['viewer.router.MainRouter']


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
# SECURE_SSL_REDIRECT = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# CORPORA = [
#     {
#         'key': 'cbc',
#         'settings_file': 'settings_viewer_cbc'
#     },
#     {
#         'key': 'arg',
#         'settings_file': 'settings_viewer_arg'
#     }
# ]
