from __future__ import absolute_import
from .base import *

from bundle_config import config

DATA_DIR = Path(config['core']['data_directory'])

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}

MEDIA_ROOT = config['core']['data_directory']

DEBUG = True
TEMPLATE_DEBUG = True

# search
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': DATA_DIR.child('whoosh_index'),
    },
}
