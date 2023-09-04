from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag
def navlink(request, pattern):
    lst_pattern = []
    if ',' in pattern:
        lst_pattern = pattern.split(',')
    else:
        lst_pattern.append(pattern)

    for pattern in lst_pattern:
        path = reverse(pattern.strip())

        if path != '/' and request.path.startswith(path):
            return 'active'

    return ''