from django import template

register = template.Library()

@register.filter
def record_type(record):
    """ Returns either 'gift' or 'wish' for a Record object """
    return type(record.child).__name__.lower()
