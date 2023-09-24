import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'common',
    'components',
    'documents',
    'files',
    'pages',
    'axes',
    'django_db_logger',
    'ckeditor',
    'solo',
    'pure_pagination',
    "compressor",
    'reset_migrations',
    'file_resubmit',
    'markdownify.apps.MarkdownifyConfig',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'nprrm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'common.context_processors.main',
            ],
        },
    },
]

WSGI_APPLICATION = 'nprrm.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_L10N = True
# DATE_FORMAT = "d-m-Y"
FORMAT_MODULE_PATH = 'common.formats'
USE_TZ = True

#--

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#--

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

#--

CODEMIRROR_PATH = "codemirror"
CODEMIRROR_MODE = "htmlmixed"

#--

CKEDITOR_CONFIGS = {
    # "default": {
    #     'toolbar': 'Basic',
    #     # "removePlugins": "image",
    #     # 'height': 700,
    #     'width': '700',
    # }
    'default': {
        'toolbar': [
            [
             '-', 'Format',
             'Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink',
             '-', 'Maximize',
            ],
        ],  
        # 'width': 900,
        # 'toolbarCanCollapse': True,
    },
}

#--

COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter',
]
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.SlimItFilter',]

#--

DJANGO_DB_LOGGER_ADMIN_LIST_PER_PAGE = 50
DJANGO_DB_LOGGER_ENABLE_FORMATTER = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'db_log': {
            'level': 'DEBUG',
            'class': 'django_db_logger.db_log_handler.DatabaseLogHandler'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': [],
            'propagate': False,
        },
        'db': {
            'handlers': ['db_log', 'mail_admins'],
            'level': 'DEBUG'
        },
        'django.request': {  # logging 500 errors to database
            'handlers': ['db_log', 'mail_admins'],
            # 'level': 'INFO',
            'level': 'ERROR',
            'propagate': False,
        }
    }
}

#--

PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 10,
    'MARGIN_PAGES_DISPLAYED': 1,

    'SHOW_FIRST_PAGE_WHEN_INVALID': False,
}

PAGINATE_BY = {
    'DEFAULT': 10,
    'NEWS': 7,
}


#--

if os.environ.get("DEBUG"):
    try:
        from nprrm.settings_docker import *
    except ImportError:
        raise ImportError("Couldn't import settings_docker.py")
else:
    try:
        from nprrm.settings_local import *
    except ImportError:
        raise ImportError("Couldn't import settings_local.py")