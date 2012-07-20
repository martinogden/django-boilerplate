from config.settings import *

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# settings/local.py is ignored to allow for easy settings
# overrides without affecting others
try:
    from local import *
except ImportError:
    pass
