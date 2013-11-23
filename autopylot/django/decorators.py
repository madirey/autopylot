from decorators import decorator
from django.conf import settings

@decorator
def require_settings(f, *args, **kwargs):
    for arg in args:
        if not hasattr(settings, arg):
            return

