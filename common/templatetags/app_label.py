from django import template

register = template.Library()

@register.filter
def app_label(obj):
    return obj._meta.app_label
