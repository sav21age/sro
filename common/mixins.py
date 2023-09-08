from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings


class CacheMixin(object):
    @method_decorator(cache_page(settings.CACHE_TIMEOUT))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)