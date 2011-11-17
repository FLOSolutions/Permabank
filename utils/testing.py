from django.test.client import Client

import unittest

class DjangoTestCase(unittest.TestCase):
    """ 
    Subclass of unittest.TestCase that implements some convenience methods
    See: http://alexgaynor.net/2010/jul/06/testing-utilities-django/
    """
    def __init__(self, *args, **kwargs):
        self.client = Client()
        super(DjangoTestCase, self).__init__(*args, **kwargs)

    def get(self, url_name, *args, **kwargs):
        return self.client.get(reverse(url_name, args=args, kwargs=kwargs))

    def post(self, url_name, *args, **kwargs):
        data = kwargs.pop("data", {})
        return self.client.post(reverse(url_name, args=args, kwargs=kwargs), data)
