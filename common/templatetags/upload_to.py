from django import template

register = template.Library()

@register.filter
def upload_to(queryset, value):
    return queryset.filter(upload_to=value)