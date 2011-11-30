from unipath import FSPath as Path

# monkey-patch python-openid to work with nycga.net
#from utils import monkey_patch_openid; monkey_patch_openid()

PROJECT_DIR = Path(__file__).absolute().ancestor(2)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ori Livneh', 'ori.livneh@gmail.com'),
)

MANAGERS = ADMINS

# needed by django-debug-toolbar
INTERNAL_IPS = ('127.0.0.1',)

# l10n / i18n
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = PROJECT_DIR.child('media')
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_DIR.child('static_root')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    str(PROJECT_DIR.child('static')),
)

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

AUTH_PROFILE_MODULE = 'profiles.Profile'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '0h&#_1@jg_o@4u6hl6rghwj^$+^qu^ads4@f^&%0%juz1rmh1t'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# OpenID Authentication
AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

OPENID_CREATE_USERS = True

# Update user details automatically when they log in
OPENID_UPDATE_DETAILS_FROM_SREG = True
OPENID_UPDATE_DETAILS_FROM_AX = True

# Use nycga.net as endpoint provider
OPENID_SSO_SERVER_URL = 'https://nycga.net/'
LOGIN_URL = '/openid/login/'
LOGIN_REDIRECT_URL = '/'
OPENID_USE_AS_ADMIN_LOGIN = False

TINYMCE_SPELLCHECKER = True
#TINYMCE_COMPRESSOR = True

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_openid_consumer.middleware.OpenIDMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates'),
)

PROJECT_APPS = (
    'profiles',
    'records',
)

EXTERNAL_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'gravatar',
    'epio_commands',
    'django_openid_auth',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_messages',
    'django.contrib.flatpages',
    'tinymce',
    'south',
)

INSTALLED_APPS = EXTERNAL_APPS + PROJECT_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

if 'grappelli' in INSTALLED_APPS:
    GRAPPELLI_ADMIN_TITLE = 'permabank'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'
