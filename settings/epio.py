from __future__ import absolute_import
from .base import *

from bundle_config import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config['postgres']['database'],
        'USER': config['postgres']['username'],
        'PASSWORD': config['postgres']['password'],
        'HOST': config['postgres']['host'],
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '{host}:{port}'.format(
                host=config['redis']['host'],
                port=config['redis']['port']),
        'OPTIONS': {
            'PASSWORD': config['redis']['password'],
        },
        'VERSION': config['core']['version'],
    },
}

MEDIA_ROOT = config['core']['data_directory']

DEBUG = True
TEMPLATE_DEBUG = True

# add solr search 
HAYSTACK_CONNECTIONS['solr'] = {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://%(host)s:%(port)s%(path)s' % config['solr']
}
