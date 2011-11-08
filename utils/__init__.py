# misc utils for permabank
from inspect import isfunction, isclass
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def requires_login(obj):
    """
    Decorator for views that ensures the user is currently logged in. Works
    both on class-based views and functions.
    """
    if isfunction(obj):  # func decorator
        f = obj
        return login_required(function=f)
    elif isclass(obj):  # class decorator
        cls = obj
        decorator = method_decorator(login_required)
        cls.dispatch = decorator(cls.dispatch)
        return cls


def monkey_patch_openid():
    """
    Patch python-openid to fix OpenID authentication with http://nycga.net/.
    
    OPENID_IDP_2_0_TYPE service is broken on nycga.net. We pop it out of the
    list of service types to coerce python-openid to default to one of the
    others. Ugly hack but it works.
    """
    # todo(ori): we should probably get to the bottom of this.
    from openid.consumer.discover import (
        OpenIDServiceEndpoint,
        OPENID_IDP_2_0_TYPE
    )

    try:
        OpenIDServiceEndpoint.openid_type_uris.remove(OPENID_IDP_2_0_TYPE)
    except ValueError:
        # class already patched!
        pass
