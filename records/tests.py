import unittest

from django.template import Context, Template

from utils.testing import DjangoTestCase
from records.models import Wish, Gift


class TestPageLoad(DjangoTestCase):
    def test_wish_browse(self):
        response = self.client.get('/wishes/all/')
        self.assertEqual(response.status_code, 200)


class TestTemplateTags(DjangoTestCase):
    def test_record_type(self):
        template = Template("{% load record_type %}"
                            "{{ record|record_type }}")
        for Type, name in ((Wish, 'wish'), (Gift, 'gift')):
            context = Context({'record': Type.objects.all()[0]})
            output = template.render(context)
            self.assertEqual(output, name)
        
if __name__ == '__main__':
    unittest.main()
