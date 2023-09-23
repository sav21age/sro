from django.conf import settings

def main(request):
    context = {
      'debug': settings.DEBUG,
      'rel_canonical': request.build_absolute_uri(request.path),
      'host': f"{request.is_secure() and 'https' or 'http'}://{request.get_host()}"
    }
    return context
