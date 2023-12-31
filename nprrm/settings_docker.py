import os
from django.conf import settings


def str2bool(s):
    if s in ('1', 'True'):
        return True
    elif s in ('0', 'False'):
        return False
    else:
        raise ValueError("Cannot covert {} to a bool".format(s))
    
def str2admins(s):
    lst_str = s.split(',')
    lst_lst = []
    for val in lst_str:
        tmp = val.strip().split(' ')
        if isinstance(tmp, list) and len(tmp) == 2:
            lst_lst.append(tmp)
    return lst_lst

DEBUG = str2bool(os.environ.get("DEBUG"))
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
SECRET_KEY = os.environ.get("SECRET_KEY")

ADMINS = str2admins(os.environ.get('ADMINS'))
LIST_OF_EMAIL_RECIPIENTS = os.environ.get("EMAIL_RECIPIENTS").split(" ")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'ATOMIC_REQUESTS': True,
    }
}

EMAIL_USE_SSL = os.environ.get("EMAIL_USE_SSL")
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")  # str comming, maybe need num
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = SERVER_EMAIL = EMAIL_HOST_USER

COMPRESS_ENABLED = True

CACHE_BACKEND = 'django.core.cache.backends.locmem.LocMemCache'
CACHE_TIMEOUT = int(os.environ.get("CACHE_TIMEOUT"))
CACHES = {
    'default': {
        'BACKEND': CACHE_BACKEND,
        'TIMEOUT': CACHE_TIMEOUT,
    },
    # 'news': {
    #     'BACKEND': CACHE_BACKEND,
    #     'TIMEOUT': CACHE_TIMEOUT,
    # },
    'axes': {
        'BACKEND': CACHE_BACKEND,
    },
    'file_resubmit': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(os.path.join(settings.BASE_DIR, 'cache'), 'file_resubmit'),
    },
}