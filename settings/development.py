from path import path
from .common import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_ROOT / 'development.sqlite3',
    }
}

DEBUG = True
THUMBNAIL_DEBUG = True


# settings/local.py is ignored to allow for easy settings
# overrides without affecting others
try:
    from local import *
except ImportError:
    pass
