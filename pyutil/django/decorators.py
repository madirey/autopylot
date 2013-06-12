from contextdecorator import ContextDecorator
from django.core.cache import cache
import json
import requests

class prime_cache(ContextDecorator):
    def __init__(self, cache_key, data_source, timeout=60*60*24):
        self.cache_key = cache_key
        self.data_source = data_source
        self.timeout = timeout

    def __enter__(self):
        data = cache.get(self.cache_key)
        if not data:
            data = json.loads(requests.get(self.data_source).text)
            cache.set(self.cache_key, data, self.timeout)
        return self

    def __exit__(self, type, value, traceback):
        return False
