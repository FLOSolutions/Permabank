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
