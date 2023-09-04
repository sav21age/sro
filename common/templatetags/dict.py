from django import template

register = template.Library()

@register.filter
def dict(dictionary, key):
    return dictionary.get(key)
