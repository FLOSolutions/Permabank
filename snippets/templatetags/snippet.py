from django import template

from snippets.models import Snippet


register = template.Library()


@register.simple_tag
def snippet(slug):
    """ Retrieves a named text snippet """
    try:
        return Snippet.get(slug)
    except Exception:
        return ''
