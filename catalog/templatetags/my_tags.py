from django import template
from django.conf import settings

register = template.Library()


@register.filter()
def media(val):
    if val:
        return f'/media/{val}'
    return '#'

