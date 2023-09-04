from django.conf import settings

def main(request):
    context = {
      'debug': settings.DEBUG,
      'cache_timeout': settings.CACHE_TIMEOUT,
      'rel_canonical': request.build_absolute_uri(),
      'host': f"{request.is_secure() and 'https' or 'http'}://{request.get_host()}"
    }
    return context
