from unipath import FSPath as Path

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
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

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
    'django.contrib.auth.backends.ModelBackend',
    'django_openid_auth.auth.OpenIDBackend',
)

OPENID_CREATE_USERS = True
OPENID_UPDATE_DETAILS_FROM_SREG = True
OPENID_SSO_SERVER_URL = 'https://www.google.com/accounts/o8/id'
LOGIN_URL = '/openid/login/'
LOGIN_REDIRECT_URL = '/'
OPENID_USE_AS_ADMIN_LOGIN = False


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates'),
)



INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'profiles',
    'epio_commands',
    'django_openid_auth',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

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

if DEBUG:
    try:
        import devserver
    except:
        pass
    else:
        INSTALLED_APPS += ('devserver',)

GRAPPELLI_ADMIN_TITLE = 'permabank'
