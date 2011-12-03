from django.template import Context, Template
from django.core.cache import cache

from snippets.models import Snippet

from utils import testing


class TestSnippets(testing.DjangoTestCase):
    def setUp(self):
        cache.clear()
        self.snippet = Snippet.objects.get_or_create(slug='hello')[0]
        self.snippet.text = "Hello, World!"
        self.snippet.save()

    def tearDown(self):
        self.snippet.delete()

    def test_template_tag(self):
        template = Template("{% load snippet %}{% snippet 'hello' %}")
        context = Context({})
        self.assertEqual(template.render(context), "Hello, World!")
        
if __name__ == '__main__':
    testing.main()
