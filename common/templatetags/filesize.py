from django import template

register = template.Library()

@register.filter
def filesize(num):
    """
    Convert bytes to KB... MB... GB... etc
    """
    lst = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    for value in lst:
        if num < 1024.0:
            if value in lst[:2]:
                return f"{num:.0f} {value}"
            return f"{num:.1f} {value}"

        num /= 1024.0


