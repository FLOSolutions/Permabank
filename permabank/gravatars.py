from urllib import urlencode
from hashlib import md5

from marcel import app

def get_gravatar_url(email, default=None, size=40):
    """ Generates a gravatar URL for a given email address """
    if default is None:
        default = app.config['DEFAULT_GRAVATAR_URL']
    email = email.lower()
    digest = md5(email).hexdigest()
    q = urlencode({'d': default, 's': size})
    return "http://www.gravatar.com/avatar/%s?%s" % (digest, q)
