from decorator import decorator
from django.core.cache import cache
import json
import requests

def prime_cache(cache_key, data_source, timeout=60*60*24):
    ''' default timeout 24 hours. '''
    def prime_cache(f, *args, **kwargs):
        data = cache.get(cache_key)
        if not data:
            data = json.loads(requests.get(data_source).text)
            cache.set(cache_key, data, timeout)
        return f()
    return decorator(prime_cache)

#@prime_cache('ships', 'http://54.235.218.58/ships?format=json')
