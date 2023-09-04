from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget


class ImageAdminWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, 'url', None):
            result = '-'
            try:
                result = '<a href="{i}" target="_blank" rel="noopener noreferrer"><img src="{i}" title="{i}"></a>'.format(
                    i=value.url
                )
                output.append(result)
            except Exception as e:
                # logger.error(e)
                pass

        output.append(super(ImageAdminWidget, self).render(name, value, attrs))

        return mark_safe(''.join(output))
